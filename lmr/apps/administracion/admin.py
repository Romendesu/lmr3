from django.contrib import admin

from django.contrib import admin
from .models import Administration

@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    # Campos que se verán en la tabla principal
    list_display = ('name', 'number', 'city', 'community', 'price', 'status', 'featured', 'created_date')
    
    # Filtros laterales para facilitar la búsqueda
    list_filter = ('status', 'community', 'featured', 'created_date')
    
    # Buscador por campos de texto
    search_fields = ('name', 'number', 'city', 'province', 'contact_email')
    
    # Campos que se pueden editar directamente desde la lista sin entrar al detalle
    list_editable = ('status', 'featured')
    
    # Organización del formulario de edición en secciones (Fieldsets)
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'number', 'status', 'featured')
        }),
        ('Ubicación', {
            'fields': ('community', 'province', 'city', 'address')
        }),
        ('Datos Económicos y Físicos', {
            'fields': ('price', 'annual_sales', 'square_meters')
        }),
        ('Contacto y Multimedia', {
            'fields': ('contact_phone', 'contact_email', 'image_url', 'description')
        }),
        ('Información del Sistema', {
            'fields': ('id', 'created_date', 'updated_date'),
            'classes': ('collapse',), # Esta sección aparece oculta por defecto
        }),
    )

    # Como el ID es un UUID no editable, lo marcamos como 'readonly' para poder verlo
    readonly_fields = ('id', 'created_date', 'updated_date')