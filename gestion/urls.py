from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # --- Añade estas líneas para solucionar el error ---
    path('registro/', views.registro_view, name='registro'), # Nombre 'registro'
    path('login/', views.login_view, name='login'),         # Nombre 'login'
    # ----------------------------------------------------
    
    # Tus otras rutas (apuntando a home por ahora)
    path('canchas/', views.home, name='canchas'),
    path('reservas/mis-reservas/', views.home, name='mis_reservas'),
    path('admin/dashboard/', views.home, name='admin_dashboard'),
    path('admin/usuarios/', views.home, name='admin_usuarios'),
    path('admin/canchas/', views.home, name='admin_canchas'),
    path('logout/', views.home, name='logout'), 
]