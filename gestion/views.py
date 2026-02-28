from django.shortcuts import render

# Dejamos las funciones de registro y login por si las necesitas luego,
# pero cambiamos la vista home para que cargue el login original.

def home(request):
    # CAMBIA AQUÍ: Regresamos a index.html (o el nombre de tu archivo de login)
    return render(request, 'gestion/index.html')

def registro_view(request):
    """Muestra la página de registro de usuario"""
    return render(request, 'gestion/registro.html')

def login_view(request):
    """Muestra la página de inicio de sesión"""
    return render(request, 'gestion/login.html')