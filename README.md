# Lmr Abogados - Sistema de Gestión

## Misión

El proyecto **Lmr Abogados** es un sistema de gestión integral diseñado para bufetes de abogados. Su misión es proporcionar una plataforma eficiente y organizada para administrar diversos aspectos del negocio legal, incluyendo la gestión de clientes, trabajadores, administraciones y funcionalidades core del sistema. Este proyecto facilita la automatización de procesos administrativos, mejora la productividad y asegura un manejo seguro y accesible de la información relacionada con casos legales, clientes y personal.

El sistema está desarrollado en Django, un framework web de Python, y está estructurado en módulos modulares (apps) para una fácil mantenibilidad y escalabilidad.

## Instalación

1. Clona o descarga el proyecto en tu máquina local.
2. Navega al directorio del proyecto: `cd LmrAbogadosDefinitivo`
3. Crea un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   venv\Scripts\activate  # En Windows
   ```
4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
5. Configura la base de datos (por defecto usa PostgreSQL):
   ```
   python lmr/manage.py migrate
   ```

## Cómo Emplear el FAKER

El directorio `faker/` contiene scripts para poblar la base de datos con datos falsos, útiles para pruebas y desarrollo. Estos scripts utilizan la biblioteca Faker para generar datos realistas.

### Para Administraciones
Ejecuta el script para agregar administraciones falsas:
```
python faker/add_fake_administrations.py
```

### Para Clientes
Ejecuta el script para agregar clientes falsos:
```
python faker/add_fake_clients.py
```

**Nota:** Asegúrate de que el servidor de Django esté corriendo y la base de datos esté configurada antes de ejecutar estos scripts. Los datos generados son aleatorios y pueden variar en cada ejecución.

## Cómo Correr el Servidor

Para ejecutar el servidor de desarrollo de Django:

1. Navega al directorio del proyecto Django: `cd lmr`
2. Ejecuta el comando:
   ```
   python manage.py runserver
   ```
3. Abre tu navegador web y ve a `http://127.0.0.1:8000/` para acceder a la aplicación.

**Nota:** Si deseas cambiar el puerto, agrega el número de puerto al comando, por ejemplo: `python manage.py runserver 8080`.

## Estructura del Proyecto

- `lmr/`: Configuración principal de Django.
- `apps/`: Módulos de la aplicación.
  - `administracion/`: Gestión de administraciones.
  - `clientes/`: Gestión de clientes.
  - `core/`: Funcionalidades core del sistema.
  - `trabajadores/`: Gestión de trabajadores.
- `faker/`: Scripts para generar datos falsos.
- `static/`: Archivos estáticos (CSS, JS, imágenes).
- `templates/`: Plantillas HTML.

## Contribución

Si deseas contribuir al proyecto, por favor sigue estos pasos:
1. Crea una rama para tu feature: `git checkout -b feature/nueva-funcionalidad`
2. Realiza tus cambios y commits.
3. Envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
