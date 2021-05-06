from django.contrib import admin
from .models import CustomUser, Category, MuscleGroup, SportType, Exercise, Diet, Plan
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
                    'plan',
                    'diet',

                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(MuscleGroup)
admin.site.register(SportType)
admin.site.register(Exercise)
admin.site.register(Diet)
admin.site.register(Plan)
