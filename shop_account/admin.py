# Core django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Local imports
from .models import User, Profile
from .forms import UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'email', 
        'username', 
        'is_active', 
        'is_admin', 
        'is_superuser'
    )
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Admin_Perm', {'fields': ('is_superuser',)}),
        ('Personal Info', {'fields': (
            'first_name',
            'last_name',
            'phone_number',
            'address',
            'city',
            'country',
            'birthday',
            'telegram_id',
            'instagram_id',
            'website',
        )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(Profile)
admin.site.unregister(Group)