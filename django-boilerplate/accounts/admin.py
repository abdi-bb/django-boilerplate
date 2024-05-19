from django.contrib import admin

# Register your models here.
from .models import CustomUser, Profile

admin.site.register(CustomUser)
admin.site.register(Profile)