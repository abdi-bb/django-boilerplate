from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext as _
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from users.models import Profile
from .exceptions import (
    AccountDisabledException,
    AccountNotRegisteredException,
    InvalidCredentialsException,
)

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class to convert Profile model instances to JSON.
    """
    class Meta:
        model = Profile
        fields = (
            'avatar',
            'bio',
            'created_at',
            'updated_at',
        )

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to convert User model instances to JSON.
    """

    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'is_active',
            'profile',
        )

class UserRegisterSerializer(RegisterSerializer):
    """
    Serializer class to register a new user using email.
    """

    username = None
    first_name = serializers.CharField(required=True, write_only=True)
    last_name = serializers.CharField(required=True, write_only=True)
    email = serializers.EmailField(required=True)

    def validate(self, validated_data):
        """
        Validate the user registration data.
        """
        
        email = validated_data.get('email', None)

        if not email:
            raise serializers.ValidationError_('Enter an email address.')
        
        if validated_data['password1'] != validated_data['password2']:
            raise serializers.ValidationError(
                _('The two password fields didn’t match.')
            )
        
        return validated_data
    
class UserLoginSerializer(serializers.Serializer):
    """
    Serializer class to login a user using email.
    """

    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    def _validate_email(self, email, password):
        """
        Validate the email and password.
        """

        user = None
        
        if email and password:
            user = authenticate(email=email, password=password)
        else:
            raise serializers.ValidationError(
                _('Must include "email" and "password".')
            )
        
        return user
    
    def validate(self, validated_data):
        """
        Validate the user login data.
        """

        email = validated_data.get('email')
        password = validated_data.get('password')

        user = None

        user = self._validate_email(email, password)

        if not user:
            raise InvalidCredentialsException()
        
        if not user.is_active:
            raise AccountDisabledException()
        
        if email:
            email_address = user.emailaddress_set.filter(
                email=user.email,
                verified=True
            ).first()
            if not email_address:
                raise serializers.ValidationError(_('Email address is not verified.'))
            
        validated_data['user'] = user

        return validated_data