from django.contrib import admin
from django.urls import path, include
from apps.core.views import home, search, autocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('catalogo/',search, name='search' ),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('informacion/', include('apps.clientes.urls'), name="contact"),
    # path('trabajadores/', include('apps.trabajadores.urls')),
    path('administracion/', include('apps.administracion.urls')),
]
