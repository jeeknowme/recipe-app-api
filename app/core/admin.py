"""
Django Admin Customizatino
"""
from core import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# 'from core import models' -> this is gonna import custom models that
#  we want to register with django admin


class UserAdmin(BaseUserAdmin):
    """Define the admin page for users"""
    ordering = ['id']
    # order them by id
    list_display = ['email', 'name']
    # list only email and name
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('Important dates'), {'fields': (['last_login'])})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': {'wide', },
            # for css
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser'
            ),
        }),  # dont forget comma here since this is a tuple
    )


admin.site.register(models.User, UserAdmin)
# UserAdmin argument is optional, if nothing is put, default user manager will
# be used with simple crud operations
