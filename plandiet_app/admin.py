from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User data',
            {
                'fields': (
                    'age',
                    'height',
                    'weight',
                    'sex',

                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)