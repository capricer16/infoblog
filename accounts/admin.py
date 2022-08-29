from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'address', 'dni')
    fieldsets = (
        *UserAdmin.fieldsets,  # campos originales del usuario
        (                      # Agregarmos nuestros campos extra
            'Información adicional',  # header, puede ser None si no se quiere agregar un header
            {
                'fields': (
                    'address',
                    'dni',
                    'role',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)