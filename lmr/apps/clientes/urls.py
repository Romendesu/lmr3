from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='information'),
    path('contacto/enviar/', views.contact_submit, name='contact_submit'),
]