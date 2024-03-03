from django.shortcuts import render, redirect

# Create your views here.

from .forms import MunicipalityForm

def registrar_municipio(request):
    if request.method == 'POST':
        form = MunicipalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirige al dashboard o a alguna otra página
    else:
        form = MunicipalityForm()

    return render(request, 'gestion_municipio/add_municipality/base.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def ver_municipios(request):
    # Lógica para mostrar los municipios
    return render(request, 'gestion_municipio/mod_municipality/base.html') #ver_municipios
