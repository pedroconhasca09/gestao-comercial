from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Perfil comercial", {"fields": ("perfil",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Perfil comercial", {"fields": ("perfil",)}),
    )

    list_display = (
        "username",
        "email",
        "perfil",
        "is_staff",
        "is_active",
    )

    list_filter = UserAdmin.list_filter + ("perfil",)