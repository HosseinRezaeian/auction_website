from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser, Documents


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        (_('Personal info'), {'fields': ('phone', 'profile_pic')}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'username', 'is_superuser', 'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'profile_pic', 'password1', 'password2', 'is_active', 'is_staff', 'username',
                       'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Documents)
