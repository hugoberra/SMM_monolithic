from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registrar/', views.registrar_municipio, name='registrar_municipio'),
    path('ver/', views.ver_municipios, name='ver_municipios'),
]
