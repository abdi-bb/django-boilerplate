from django.contrib import admin

# Register your models here.
from .models import CustomUser, Profile

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'activeness')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
