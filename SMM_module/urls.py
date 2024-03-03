from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registrar/', views.registrar_municipio, name='registrar_municipio'),
    path('ver/', views.ver_municipios, name='ver_municipios'),
    path('eliminar/<int:id>/', views.eliminar_municipio, name='eliminar_municipio'),
    path('modificar/<int:id>/', views.modificar_municipio, name='modificar_municipio'),
]
