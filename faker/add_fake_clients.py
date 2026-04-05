import os
import sys
import django
import random
from faker import Faker
from dotenv import load_dotenv

# 1. Cargar variables de entorno (.env está en la raíz, una carpeta atrás de faker/)
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# 2. Configurar rutas para que Python encuentre 'apps'
# BASE_DIR es la raíz del proyecto (donde está .env)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Añadimos la carpeta 'lmr' al path porque es la que contiene a 'apps'
sys.path.append(os.path.join(BASE_DIR, 'lmr'))

# 3. Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lmr.settings')
django.setup()

# 4. Importar el modelo (Ahora sí lo encontrará dentro de lmr/apps/...)
from apps.clientes.models import ClienteContacto 

def populate_contactos(n=15):
    fake = Faker('es_ES')
    print(f"--- Iniciando población de Contactos ---")

    # Extraemos las opciones válidas del modelo
    intereses_choices = [c[0] for c in ClienteContacto.TIPO_INTERES_CHOICES]

    for _ in range(n):
        nombre_fake = fake.name()
        
        # Simulamos mensajes realistas
        mensajes_ejemplo = [
            f"Hola, estoy interesado en el traspaso de la administración en {fake.city()}.",
            "¿Podrían enviarme más información detallada por correo?",
            "Me gustaría concertar una cita para hablar sobre la asesoría jurídica.",
            f"Solicito información sobre el punto de venta mixto que tienen en {fake.profile()}.",
            "¿Cuáles son los requisitos para la compra de una administración integral?"
        ]

        # Algunos tienen observaciones de administración, otros no (40% de probabilidad)
        obs_internas = None
        if random.random() > 0.6:
            obs_internas = random.choice([
                "Interesado serio, llamar lo antes posible.",
                "Enviado dossier por email.",
                "Falta confirmación de presupuesto.",
                "Viene recomendado por despacho asociado."
            ])

        # Creamos el registro
        contacto = ClienteContacto.objects.create(
            nombre=nombre_fake,
            email=fake.email(),
            telefono=fake.phone_number() if random.choice([True, False]) else None,
            interes=random.choice(intereses_choices),
            mensaje=random.choice(mensajes_ejemplo),
            observaciones=obs_internas
        )

        print(f"✅ Creado: {contacto.nombre} | Interés: {contacto.get_interes_display()}")

if __name__ == '__main__':
    # Ejecutamos la función
    populate_contactos(10)
    print("--- Proceso terminado con éxito ---")