from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'level', 'gremio', 'gold', 'is_staff')
    list_filter = ('role', 'gremio', 'level', 'is_staff')

    fieldsets = UserAdmin.fieldsets + (
        ('Atributos de Héroe', {
            'fields': ('role', 'level', 'experience', 'gold', 'gremio'),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Atributos de Héroe', {
            'fields': ('role', 'level', 'experience', 'gold', 'gremio'),
        }),
    )

