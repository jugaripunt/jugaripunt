from django.db import models

# Model que representa un jugador
class Jugador(models.Model):
    id = models.AutoField(primary_key=True)  # Identificador únic per a cada jugador
    nom = models.CharField(max_length=50)  # Nom del jugador (max. 50 caràcters)
    cognoms = models.CharField(max_length=100)  # Cognoms del jugador (max. 100 caràcters)
    edat = models.IntegerField()  # Edat del jugador (sencer)
    email = models.EmailField()  # Correu electrònic del jugador (format de correu electrònic)
    num_federat = models.IntegerField(default=0) #numero de federat del jugador (numeric)
    contrasenya = models.CharField(max_length=128)  # Contrasenya del jugador (max. 128 caràcters)
    session_token = models.CharField(max_length=255, blank=True, null=True)  # Camp opcional per al token de sessió

    def __str__(self):
        return self.nom  # Retorna el nom del jugador com a representació en cadena
