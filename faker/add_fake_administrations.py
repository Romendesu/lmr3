import os
import sys
import django
import random
from faker import Faker
from dotenv import load_dotenv

# 1. Cargar variables de entorno (buscando el .env que está una carpeta atrás)
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# 2. Ajustar el PATH para que Python encuentre la carpeta 'lmr'
# Conseguimos la ruta de la raíz: LmrAbogadosDefinitivo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 3. Añadimos la carpeta interna 'lmr' donde está el manage.py
sys.path.append(os.path.join(BASE_DIR, 'lmr'))

# 4. Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lmr.settings')
django.setup()

# 5. Importar modelos (ahora ya debería encontrarlos)
from apps.administracion.models import Administration, CommunityEnum, StatusEnum

def populate(n=1000):
    fake = Faker('es_ES')
    print(f"--- Iniciando población en PostgreSQL ---")

    # Obtenemos los valores de los enums
    communities = [c[0] for c in CommunityEnum.choices]
    statuses = [s[0] for s in StatusEnum.choices]

    for _ in range(n):
        nombre = f"Lotería {fake.last_name()} {fake.word().capitalize()}"
        
        admin = Administration.objects.create(
            name=nombre,
            number=str(random.randint(1, 150)),
            community=random.choice(communities),
            province=fake.administrative_unit(), 
            city=fake.city(),
            address=fake.street_address(),
            price=round(random.uniform(50000, 500000), 0),
            annual_sales=round(random.uniform(500000, 3000000), 0),
            square_meters=round(random.uniform(25, 120), 1),
            description=fake.paragraph(nb_sentences=3),
            image_url=f"https://picsum.photos/id/{random.randint(1, 100)}/800/600",
            status=random.choice(statuses),
            featured=random.choice([True, False]),
            contact_phone=fake.phone_number(),
            contact_email=fake.company_email()
        )
        print(f"✅ Creada: {admin.name} en {admin.city}")
if __name__ == '__main__':
    populate(12)