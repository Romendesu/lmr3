from django.urls import path
from . import views

urlpatterns = [
    path('administracion/<uuid:pk>/', views.administration_detail, name='administration_detail'),
]