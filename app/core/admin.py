"""
Django Admin Customizatino
"""
from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# 'from core import models' -> this is gonna import custom models that
#  we want to register with django admin


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users"""
    ordering = ['id']
    # order them by id
    list_display = ['email', 'name']
    # list only email and name


admin.site.register(models.User, UserAdmin)
# UserAdmin argument is optional, if nothing is put, default user manager will
# be used with simple crud operations
