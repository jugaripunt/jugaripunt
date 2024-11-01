from django.urls import path
from . import views

urlpatterns = [
    path('jugador', views.crear_jugador, name='crear_jugador/'),  # Ruta per a crear el jugador
    path('login', views.login_view, name='login/'),  # Ruta per a la comprovació del login
    path('logout', views.logout_view, name='logout/'),  # Ruta per a la comprovació del login
    path('noutorneig', views.creatorneig_view, name='creartorneig/'),  # Ruta per a la creació d'un nou torneig
    path('torneig/afegir_jugadors', views.afegirJugadors_view, name='afegirjugador/'),  # Ruta per a la creació d'un nou torneig


]
