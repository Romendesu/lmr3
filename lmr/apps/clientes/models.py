from django.db import models
from django.db import models

class ClienteContacto(models.Model):
    # Opciones para el campo 'interes' (basado en tu select de HTML)
    TIPO_INTERES_CHOICES = [
        ('integral', 'Traspaso Administración Integral'),
        ('mixto', 'Punto de Venta Mixto'),
        ('asesoria', 'Asesoría Jurídica / Fiscal'),
    ]

    # Campos del formulario
    nombre = models.CharField(max_length=150, verbose_name="Nombre completo")
    email = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")
    interes = models.CharField(
        max_length=20, 
        choices=TIPO_INTERES_CHOICES, 
        verbose_name="Tipo de activo de interés"
    )
    mensaje = models.TextField(verbose_name="Mensaje del cliente")

    # Campos de gestión interna
    fecha_contacto = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de recepción")
    
    # Campo solicitado: Observaciones (solo para administración)
    observaciones = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Observaciones internas",
        help_text="Notas privadas para el despacho sobre este cliente."
    )

    class Meta:
        verbose_name = "Consulta de Cliente"
        verbose_name_plural = "Consultas de Clientes"
        ordering = ['-fecha_contacto']

    def __str__(self):
        return f"{self.nombre} - {self.get_interes_display()}"