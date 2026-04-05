import uuid
from django.db import models

# Enumeración de las comunidades autónomas
class CommunityEnum(models.TextChoices):
    ANDALUCIA = 'ANDALUCIA', 'Andalucía'
    ARAGON = 'ARAGON', 'Aragón'
    ASTURIAS = 'ASTURIAS', 'Asturias'
    BALEARES = 'BALEARES', 'Islas Baleares'
    CANARIAS = 'CANARIAS', 'Canarias'
    CANTABRIA = 'CANTABRIA', 'Cantabria'
    CASTILLA_LA_MANCHA = 'CASTILLA_LA_MANCHA', 'Castilla-La Mancha'
    CASTILLA_Y_LEON = 'CASTILLA_Y_LEON', 'Castilla y León'
    CATALUNYA = 'CATALUNYA', 'Cataluña'
    COMUNITAT_VALENCIANA = 'COMUNITAT_VALENCIANA', 'Comunidad Valenciana'
    EXTREMADURA = 'EXTREMADURA', 'Extremadura'
    GALICIA = 'GALICIA', 'Galicia'
    MADRID = 'MADRID', 'Comunidad de Madrid'
    MURCIA = 'MURCIA', 'Región de Murcia'
    NAVARRA = 'NAVARRA', 'Navarra'
    PAIS_VASCO = 'PAIS_VASCO', 'País Vasco'
    LA_RIOJA = 'LA_RIOJA', 'La Rioja'
    CEUTA = 'CEUTA', 'Ceuta'
    MELILLA = 'MELILLA', 'Melilla'

class StatusEnum(models.TextChoices):
    AVAILABLE = 'AVAILABLE', 'Disponible'
    RESERVED = 'RESERVED', 'Reservada'
    SOLD = 'SOLD', 'Vendida'

class Administration(models.Model):
    # Usamos UUID como llave primaria según el ínice
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    # Fechas automáticas
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    # Datos básicos
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=50, blank=True, null=True) # Ej: Admon Nº 5
    
    # Ubicación
    community = models.CharField(
        max_length=50, 
        choices=CommunityEnum.choices,
        default=CommunityEnum.MADRID
    )
    province = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    
    # Datos económicos y físicos
    price = models.FloatField() # double precision
    annual_sales = models.FloatField(blank=True, null=True)
    square_meters = models.FloatField(blank=True, null=True)
    
    # Información adicional
    description = models.TextField(blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True) # O models.URLField()
    
    # Estado y visibilidad
    status = models.CharField(
        max_length=20,
        choices=StatusEnum.choices,
        default=StatusEnum.AVAILABLE
    )
    featured = models.BooleanField(default=False)
    
    # Contacto
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    contact_email = models.EmailField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'administrations'
        verbose_name = 'Administración'
        verbose_name_plural = 'Administraciones'
        ordering = ['-created_date']

    def __str__(self):
        return f"{self.name} - {self.city}"