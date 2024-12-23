from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('jugador', views.crear_jugador, name='crear_jugador'), # Ruta per a crear el jugador
    path('recuperar_password', views.recuperar_password, name='recuperar_password'), #recupera el password
    path('modificar_password', views.modificar_password, name='modificar_password'), #modifica el password
    path('login', views.login_view, name='login'), # Ruta per a la comprovació del login
    path('logout', views.logout_view, name='logout'), # Ruta per a la comprovació del login
    path('noutorneig', views.crear_torneig, name='creartorneig'), # Ruta per a la creació d'un nou torneig
    path('dashboard/<int:jugador_id>', views.getUser_view, name='infoJugador'),
    path('partides', views.getPartides, name='getPartides'), # Ruta per obtenir les partides
    path('registreresultat', views.registrarResultatPartida, name='registreresultat'), # Ruta per a registrar resultats
    path('jugador/buscar', views.buscar_jugador, name='buscar_jugador'),
    path('lligues', views.getLligues, name="getLligues"),
    path('exportarResultats', views.exportar_resultats, name="exportarResultats"),
    path('resultatslliga', views.getResultatsLliga, name='getResultatsLliga'), # Ruta per obtenir els resultats d'una lliga
    path('ranking', views.get_ranking, name='get_ranking'), # Ruta per obtenir el ranking
    path('classificacio/', views.get_classificacioLliga, name='classificacio'), # Ruta per obtenir el ranking

]
