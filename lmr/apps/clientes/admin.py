from django.contrib import admin

from django.contrib import admin
from .models import ClienteContacto
from django.utils.html import format_html

@admin.register(ClienteContacto)
class ClienteContactoAdmin(admin.ModelAdmin):
    # 1. Columnas que se ven en la lista principal
    list_display = ('nombre_con_icono', 'email', 'telefono', 'get_interes_badge', 'fecha_contacto', 'tiene_observaciones')
    
    # 2. Filtros laterales para encontrar rápido a los clientes
    list_filter = ('interes', 'fecha_contacto')
    
    # 3. Buscador (busca por nombre, email o el contenido del mensaje)
    search_fields = ('nombre', 'email', 'mensaje', 'observaciones')
    
    # 4. Configuración del formulario de edición (Detalle)
    fieldsets = (
        ('Información del Cliente', {
            'fields': ('nombre', 'email', 'telefono')
        }),
        ('Detalles de la Consulta', {
            'fields': ('interes', 'mensaje', 'fecha_contacto'),
        }),
        ('Gestión Interna', {
            'fields': ('observaciones',),
            'description': 'Escribe aquí el seguimiento o notas privadas sobre este cliente.'
        }),
    )

    # 5. La fecha no se puede editar, es automática
    readonly_fields = ('fecha_contacto',)

    # --- MÉTODOS PARA MEJORAR EL DISEÑO VISUAL ---

    @admin.display(description='Interés')
    def get_interes_badge(self, obj):
        colors = {
            'integral': '#066a4c', # Verde oscuro
            'mixto': '#0d6efd',    # Azul
            'asesoria': '#6c757d', # Gris
        }
        color = colors.get(obj.interes, '#000')
        return format_html(
            '<span style="color: white; background-color: {}; padding: 3px 10px; border-radius: 10px; font-size: 11px; font-weight: bold;">{}</span>',
            color,
            obj.get_interes_display()
        )

    @admin.display(description='Cliente')
    def nombre_con_icono(self, obj):
        return format_html('<i class="bi bi-person-fill"></i> {}', obj.nombre)

    @admin.display(description='Obs.', boolean=True)
    def tiene_observaciones(self, obj):
        """Muestra un check verde si ya tiene notas escritas"""
        return bool(obj.observaciones)