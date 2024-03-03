from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def registrar_municipio(request):
    # Lógica para el formulario de registro
    return render(request, 'gestion_municipio/add_municipality/base.html') # registrar

def ver_municipios(request):
    # Lógica para mostrar los municipios
    return render(request, 'gestion_municipio/mod_municipality/base.html') #ver_municipios
