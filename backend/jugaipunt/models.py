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
    admin = models.BooleanField(default=False)  # per controlar si es o no administrador
    session_token = models.CharField(max_length=255, blank=True, null=True)  # Camp opcional per al token de sessió

    def __str__(self):
        return self.nom  # Retorna el nom del jugador com a representació en cadena


    # DFA - Model per la partida - en construcció
    #class Partida(models.Model):
        #idPartida = # asignem una ID a la partida
        #data = models.DateField() #data informada de la partida
        #jugador1 = # Porta la ID del emparallement i mostra concatenats nom i cognom.
        #jugador2 = # Porta la ID del emparallement i mostra concatenats nom i cognom.
        #resultat = #ha de portar el valor resultat de la partida asociat a la id

        #def __str__(self):
            #return #ha de retornar el nom de la partida, els jugadors amb el seu resultats i la data. el valor retornat s'utilitzara per les lligues id -> resultat


    # Eudald- Model per la lliga - en construcció
    #class Lliga(models.Model):
        #NomLLiga = models.CharField(max_length=50)  # Nom de la lliga (max. 50 caràcters)
        #data = models.DateField() #data informada de la lliga
        #ubicacio = #ubicacio geografica de la lliga. es podria asociar a futur a mapa
        #torneigEliminatori = #valor true or false
        #usuariAdmin = #admin associat per ID
        #resultat = #guanyador de la lliga amb ID

        #def __str__(self):
            #return #ha de retornar el nom de la lliga i els seus camps en cadena