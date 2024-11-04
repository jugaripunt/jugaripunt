from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import get_random_string 
import json
from .models import Jugador

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
                    'token': session_token  # Devuelve el token
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


# DFA Funció per a retornar un JSON amb el nom i cognoms del jugador a partir d'una ID
@csrf_exempt
def jugador_nomComplet(request, jugador_id):
    try:
        # busquem el jugador per la ID
        jugador = Jugador.objects.get(id=jugador_id)
    except Jugador.DoesNotExist:
        # Si no el troba, retornem un error en un JSON
        return JsonResponse({'error': 'Jugador no trobat.'}, status=404)

    # en Cas que SI existeixi, creem el JSON portant el nom i els cognoms
    nomJugador = {
        'nom_complet': f"{jugador.nom} {jugador.cognoms}"
    }
    # Retornem el nom del jugador perquè es pugui utilitzar
    return JsonResponse(nomJugador)

#@csrf_exempt
#def creatorneig_view(request):
#funció per a crear tornejos, descomentem i creem les lògiques

#@csrf_exempt
#def afegirJugadors_view(request):
#funció per afegir els jugadors al torneig (des del frontend s'envien en una list, no jugador per jugador)

#@csrf_exempt
#def crearPartida_view(request):
#funció per crear la partida en aleatori mitjançant dos ID random de jugadors, crea una id de partida i sobre aquesta es la que es guardaran els resultats

#DFA funció per a retornar les dades de l'usuari, totes, si és admin, nom, cognom, partides en les que està
@csrf_exempt
def getUser_view(request, jugador_id):
    try:
        # busquem el jugador per la ID
        jugador = Jugador.objects.get(id=jugador_id)
    except Jugador.DoesNotExist:
        # error en cas que no el trobi
        return JsonResponse({'error': 'Jugador no trobat.'}, status=404)

    # Si troba la ID, crearem un JSON amb els valors existents. podem ampliar si a futur posem mes
    jugador_data = {
        'id': jugador.id,
        'nom': jugador.nom,
        'cognoms': jugador.cognoms,
        'edat': jugador.edat,
        'email': jugador.email,
        'num_federat': jugador.num_federat,
        'admin': jugador.admin
    }
    # Retornem les dades del jugador en un JSON
    return JsonResponse(jugador_data)

#DFA funció per a afegir els resultats de les partides. Data, usuari guanyador i perdedor. ens portem el resultat de un desplegable
@csrf_exempt
def afegir_resultats(request, id_partida, id_jugador, resultat):
    try:
        # ens portem la ID de la partida que s'ha generat en l'aleatori
        partida = Partida.objects.get(id=id_partida)
    except Partida.DoesNotExist:
        # si no troba la partida tornar un JSON amb l'error
        return JsonResponse({'error': 'Partida no trobada.'}, status=404)

    try:
        # ara busquem al jugador per ID per veure que existeix
        jugador = Jugador.objects.get(id=id_jugador)
    except Jugador.DoesNotExist:
        # Si no troba el jugador tornar un JSON amb l'error
        return JsonResponse({'error': 'Jugador no trobat.'}, status=404)

    # posem un control per si el desplegable  de resultat ve buit
    if resultat not in ['guanyador', 'perdedor']:
        return JsonResponse({'error': 'Resultat no vàlid. Utilitzeu "guanyador" o "perdedor".'}, status=400)

    # Actualitzem el resultat segons el desplegable
    if resultat == 'guanyador':
        partida.guanyador = jugador
        # per defecte nomes pot haber un guanyador i l'altre usuari automaticament es perdedor
        partida.perdedor = partida.jugador2 if jugador.id == partida.jugador1.id else partida.jugador1
    elif resultat == 'perdedor':
        partida.perdedor = jugador
        # la inversa, si el jugador es perdedor, l'altre usuari automaticament es guanyador
        partida.guanyador = partida.jugador1 if jugador.id == partida.jugador2.id else partida.jugador2

    # Guardem l'assignació a la partida
    partida.save()

    # Retornem un JSON indicant qui es el guanyador i perdedor perque la llogica de lliga el pugui utilitzar
    return JsonResponse({
        'guanyador': partida.guanyador.id,
        'perdedor': partida.perdedor.id,
        'missatge': 'Resultat actualitzat a la partida'
    })




