from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string
import json
from .models import Jugador, Lliga, Partida

@csrf_exempt
def crear_jugador(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Comprovar si el jugador ja existeix per email o nom
            if Jugador.objects.filter(email=data.get('email')).exists():
                return JsonResponse({'error': 'Ja existeix un jugador amb aquest correu electrònic.'}, status=400)

            if Jugador.objects.filter(nom=data.get('nom')).exists():
                return JsonResponse({'error': 'Ja existeix un jugador amb aquest nom.'}, status=400)

            # Hashear la contrasenya abans de guardar
            data['contrasenya'] = make_password(data.get('contrasenya'))

            # Crear el jugador
            jugador = Jugador.objects.create(**data)

            return JsonResponse({'message': 'Jugador creat exitosament!'}, status=201)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            contrasenya = data.get('contrasenya')

            try:
                jugador = Jugador.objects.get(email=email)
            except Jugador.DoesNotExist:
                return JsonResponse({'error': 'Jugador no trobat.'}, status=404)

            # Comprovar la contrasenya utilitzant check_password
            if check_password(contrasenya, jugador.contrasenya):
                # Generar un token de sessió
                session_token = get_random_string(length=32)

                # Guardar el token a la base de dades del jugador
                jugador.session_token = session_token
                jugador.save()

                return JsonResponse({
                    'message': f'Benvingut, {jugador.nom}!',
                    'nom_usuari': jugador.nom,
                    'id_usuari': jugador.pk, # retorna id usuari
                    'token': session_token,  # Devuelve el token
                    'admin': jugador.admin
                }, status=200)
            else:
                return JsonResponse({'error': 'Contrasenya incorrecta.'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Sol·licitud invàlida.'}, status=400)

    return JsonResponse({'error': 'Mètode no permès'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            token = data.get('token')

            try:
                # Buscar al jugador que tiene el token de sesión dado
                jugador = Jugador.objects.get(session_token=token)
            except Jugador.DoesNotExist:
                return JsonResponse({'error': 'Token de sessió no vàlid.'}, status=404)

            # Eliminar el token de sesión
            jugador.session_token = None
            jugador.save()

            return JsonResponse({'message': 'Sessió tancada correctament.'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Sol·licitud invàlida.'}, status=400)

    return JsonResponse({'error': 'Mètode no permès'}, status=405)

@csrf_exempt
def crear_torneig(request):
    if request.method == "POST":
        # Cargar los datos JSON del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Extraer datos de la liga y la lista de jugadores
        nomLliga = data.get("nomLliga")
        dataInici = data.get("dataInici")
        dataFi = data.get("dataFi")
        tipusTorneig = data.get("tipusTorneig")
        llistaJugadors = data.get("llistaJugadors", [])
        usuari_id = data.get("usuari")

        # Obtener el jugador administrador
        try:
            usuari = Jugador.objects.get(id=usuari_id)
        except Jugador.DoesNotExist:
            return JsonResponse({"error": "Usuario no encontrado"}, status=404)

        if not usuari.admin:
            return JsonResponse({"error": "El jugador no es administrador"}, status=403)

        # Crear la liga
        lliga = Lliga.objects.create(
            nomLliga=nomLliga,
            dataInici=dataInici,
            dataFi=dataFi,
            tipusTorneig=tipusTorneig,
            usuariAdmin=usuari  # Asume que el jugador es el administrador
        )

        # Obtener los jugadores y asignarlos a la liga
        jugadors = []
        for jugador_data in llistaJugadors:
            jugador_id = jugador_data.get("id")
            if jugador_id:
                jugador = get_object_or_404(Jugador, id=jugador_id)
                jugadors.append(jugador)

        # Asignar jugadores a la liga utilizando 'set()' para ManyToMany
        lliga.llistaJugadors.set(jugadors)

        # Generar las partidas si el tipo de torneo es "liga"
        if tipusTorneig == "Lliga":
            jugadors = list(lliga.llistaJugadors.all())  # Obtener todos los jugadores asociados a la liga
            for i in range(len(jugadors)):
                for j in range(i + 1, len(jugadors)):
                    Partida.objects.create(
                        lliga=lliga,
                        jugador1=jugadors[i],
                        jugador2=jugadors[j]
                    )

        return JsonResponse({"message": "Lliga creada amb èxit i partides generades!"}, status=201)

    return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def getUser_view(request, jugador_id):
    try:
        # Buscamos el jugador por su ID
        jugador = Jugador.objects.get(id=jugador_id)
    except Jugador.DoesNotExist:
        # Error en caso de que no lo encuentre
        return JsonResponse({'error': 'Jugador no trobat.'}, status=404)

    # Datos del jugador
    jugador_data = {
        'id': jugador.id,
        'nom': jugador.nom,
        'cognoms': jugador.cognoms,
        'edat': jugador.edat,
        'email': jugador.email,
        'num_federat': jugador.num_federat,
        'admin': jugador.admin,
    }

    # Listar todas las ligas en las que participa el jugador
    lligues = jugador.lligues.all()
    lligues_data = []
    for lliga in lligues:
        # Solo devolvemos el nombre de la liga
        lligues_data.append({
            'lliga_id': lliga.id,
            'nomLliga': lliga.nomLliga
        })

    # Añadimos la información de las ligas al JSON de respuesta del jugador
    jugador_data['lligues'] = lligues_data

    # Listar todas las partidas en las que el jugador participa
    partides_data = []
    partides = Partida.objects.filter(jugador1=jugador) | Partida.objects.filter(jugador2=jugador)
    for partida in partides:
        # Determinamos el contrincante
        contrincant = partida.jugador2 if partida.jugador1 == jugador else partida.jugador1
        partides_data.append({
            'partida_id': partida.id,
            'contrincant': {
                'id': contrincant.id,
                'nom': contrincant.nom,
                'cognoms': contrincant.cognoms
            },
            'resultat': partida.get_resultat_display() if partida.resultat else "Pendiente"
        })

    # Añadimos las partidas al JSON de respuesta del jugador
    jugador_data['partides'] = partides_data

    # Retornamos todos los datos del jugador, incluyendo las ligas (solo nombre) y partidas
    return JsonResponse(jugador_data)

@csrf_exempt
def getPartides(request):
    """Funció per a retornar totes les partides"""

    partides = Partida.objects.all()

    llista_partides = []

    for partida in partides:
        llista_partides.append({
            'partida_pk': partida.pk,
            'jugador1': partida.jugador1.nom,
            'jugador1_pk': partida.jugador1.pk,
            'jugador2': partida.jugador2.nom,
            'jugador2_pk': partida.jugador2.pk,
        })

    return JsonResponse(llista_partides, safe=False)

@csrf_exempt
def registrarResultatPartida(request):
    """Funció per a registrar els resultats de les partides"""

    if request.method == "POST":
        # Cargar los datos JSON del cuerpo de la solicitud
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data"}, status=400)

        # Dades resultat
        partida_pk = data.get("partida_pk")
        guanyador = data.get("guanyador")

        print(partida_pk)
        print(guanyador)

        partida = Partida.objects.filter(pk=partida_pk)

        if(guanyador == 'jugador1'):
            partida.update(resultat='VJ1')
        if(guanyador == 'jugador2'):
            partida.update(resultat='VJ2')
        if(guanyador == 'EMP'):
            partida.update(resultat='EMP')


        return JsonResponse({"message": "S'ha desat el resultat amb èxit!"}, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

@csrf_exempt
def buscar_jugador(request):
    # Obtener el parámetro 'nom' de la query string
    nom = request.GET.get('nom', '')

    if nom:
        # Filtramos los jugadores cuyo nombre contiene el valor de 'nom'
        jugadores = Jugador.objects.filter(nom__icontains=nom)
    else:
        jugadores = Jugador.objects.none()

    # Creamos una lista de diccionarios con los datos que queremos devolver
    jugadores_data = list(jugadores.values('id', 'nom', 'cognoms'))  # Puedes agregar más campos si lo deseas

    # Devolvemos los datos en formato JSON
    return JsonResponse(jugadores_data, safe=False)

#@csrf_exempt
#def getUser_view(request):
#funció per a retornar les dades de l'usuari, totes, si és admin, nom, cognom, partides en les que està

#@csrf_exempt
#def afegir_resultats(request):
#funció per a afegir els resultats de les partides. Data, usuari guanyador i perdedor.