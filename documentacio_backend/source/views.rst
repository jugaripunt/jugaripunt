Django Views Documentation
===========================

Documentació de les funcions implementades a la vista del projecte. 


Function-Based Views
--------------------

.. autofunction:: myapp.views.sample_view


crear_jugador
=============

.. function:: crear_jugador(request)


  La función `crear_jugador` permet la creació d'un nou jugador a la base de dades a través d'una sol·licitud HTTP `POST`.

  Decoradors:
      - :decorator:`@csrf_exempt`: Eximeix la vista de la protecció contra CSRF. 

  Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP enviada al client. Ha de contenir un cos JSON amb les dades necessàries per a crear un jugador. 


  Cos de la sol·licitud:
    - El cos de la sol·licitud ha de ser un JSON amb els següents camps obligatòris:

    - `email` (str): El correu electrònic del jugador. Ha de ser únic. 
    - `nom` (str): El nom del jugadador. Ha de ser únic. 
    - `contrasenya` (str): La contrasenya del jugador. S'emmagatzemarà de forma segura després de ser encriptada. 

  Flux d'execució
    1. Comproba que el mètode de la sol·licitud és `POST`. 
    2. Intenta parsejar el cos JSON de la sol·licitud. 
    3. Valida que no existeixi ja un jugador amb el maeix correu electrònic o nom. 
    4. Encripta la contrasenya proporcionada. 
    5. Crea un nou objecte `Jugador` amb les dades proporcionades. 
    6. Retorna una resposta JSON indicant l'èxit o error de l'operació. 

  Respostes
    - **201 Created**: 
      Si el jugador s'ha creat amb èxit. Exemple:

      .. code-block:: json

        {
            "message": "Jugador creat exitosament!"
        }

    - **400 Bad Request**: 
      Si s'ha produït un error en el procés, com per exemple: 
      
      - Ja existeix un jugador amb el mateix correu o nom. 
      - Error en les dades enviades.

      Exemple:

      .. code-block:: json

        {
            "error": "Ja existeix un jugador amb aquest correu electrònic."
        }

  Exemple d'ús


    - **Sol·licitud**

    .. code-block:: http

      POST /crear_jugador/ HTTP/1.1
      Content-Type: application/json

      {
          "email": "jugador@example.com",
          "nom": "Jugador1",
          "contrasenya": "mi_contrasenya_secreta"
      }

    - **Resposta**

    .. code-block:: http

      HTTP/1.1 201 Created
      Content-Type: application/json

      {
          "message": "Jugador creat exitosament!"
      }


login_view
==========

Vista per a gestionar l'inici d'una sessió dels usuaris de l'aplicació.

.. function:: login_view(request)

   Aquesta vista permet als usuaris iniciar sessió proporcionant el seu correu electrònic i password. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La solicitud HTTP rebuda per el servidor.

   Mètodes HTTP:
      - **POST**: Aquest és l'únic mètode permès. Processa la sol·licitud per a l'inici de sessió de l'usuari. 

   Entrades (POST):
      La sol·licitud ha d'incloure un cos JSON amb els següents camps:
      
      - **email** (str): El correu electrònic de l'usuari. 
      - **contrasenya** (str): La contrasenya de l'usuari.

   Respostes:
      - **200 OK**: Si les credencials son vàlides. 
      
        El cos de la resposta inclou: 
          - **message** (str): Un missatge de benvinguda.
          - **nom_usuari** (str): Nom de l'usuari.
          - **id_usuari** (int): ID de l'usuari a la base de dades.
          - **token** (str): Token de sessió generat. 
          - **admin** (bool): Indica si l'usuari té privilegis d'administrador. 

      - **400 Bad Request**: Si hi ha errors a la sol·licitud, com: 
          - Contrasenya incorrecta.
          - Cos JSON invàlid.

      - **404 Not Found**: Si no es troba un usuari amb el correu electrònic proporcionat. 

      - **405 Method Not Allowed**: Si s'usa un mètode HTTP diferent a POST.  

   Exemple de sol·licitud:
      .. code-block:: http

         POST /login_view/ HTTP/1.1
         Content-Type: application/json

         {
             "email": "usuario@example.com",
             "contrasenya": "password123"
         }

   Exemple de resposta (200 OK):
      .. code-block:: json

         {
             "message": "Benvingut, Juan!",
             "nom_usuari": "Juan",
             "id_usuari": 123,
             "token": "abcd1234efgh5678ijkl9012mnop3456",
             "admin": false
         }


recuperar_password
==================

Vista per a validar les dades proporcionades per l'usuari i confirmar la seva identitat per a la recuperació de la contrasnya. 

.. function:: recuperar_password(request)

   Aquesta vista permet als usuris verificar la seva identitat proporcionant la seva informació personal. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda pel servidor. 

   Mètodes HTTP:
      - **POST**: Aquest és l'únic mètode permès. Valida les dades de l'usuari. 

   Entrades (POST):
      La sol·licitud ha d'incloure un cos JSON amb els següents camps: 
      
      - **nom** (str): Nom d'usuari.
      - **cognoms** (str): Cognoms.
      - **email** (str): Correu electrònic.
      - **edat** (int): Edat de l'usuari.

   Respostes:
      - **200 OK**: Si les dades proporcionades son correctes. 
      
        El cos de la resposta inclou: 
          - **message** (str): Un missatge indicant que les dades son correctes. 

      - **400 Bad Request**: Si alguna de les dades proporcionades no coincideix amb un usuari de la base de dades. 

      - **405 Method Not Allowed**: Si s'usa un mètode HTTP diferent a POST.

   Exemple de sol·licitud: 
      .. code-block:: http

         POST /recuperar_password/ HTTP/1.1
         Content-Type: application/json

         {
             "nom": "Juan",
             "cognoms": "Pérez",
             "email": "juan.perez@example.com",
             "edat": 30
         }

   Exemple de resposta (200 OK):
      .. code-block:: json

         {
             "message": "Dades correctes."
         }

   Exemple de respuesta (400 Bad Request):
      .. code-block:: json

         {
             "error": "Algunes dades no són correctes."
         }

   Notes:
      - Aquesta vista no realitza cap canvi a la base de dades ni envia informació adicional. Només valida les dades proporcionades. 
      - És important que el client usi HTTPS per a protegir les dades sensibles durant la transmissió. 

modificar_password
==================

Vista per a modificar la contrasenya d'un usuari després de validar la seva identitat. 

.. function:: modificar_password(request)

   Aquesta vista permet als usuaris actualitzar la seva contrasenya després de confirmar les seves dades personals. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda per el servidor. 

   Mètodes HTTP:
      - **POST**: Aquest és l'únic mètode permès. Modifica la contrasenya de l'usuari si les dades son vàlides. 

   Entrades (POST):
      La sol·licitud ha d'incloure un cos JSON amb els següents camps: 
      
      - **nom** (str): Nom de l'usuari.
      - **cognoms** (str): Cognoms de l'usuari. 
      - **email** (str): Correu electrònic de l'usuari. 
      - **edat** (int): Edat de l'usuari. 
      - **novaContrasenya** (str): Nova contrasenya que s'establirà per a l'usuari. 

   Respostes:
      - **200 OK**: Si les dades son vàlides i la contrasenya s'ha actualitzat correctament. 
      
        El cos de la resposta inclou: 
          - **message** (str): Missatge de confirmació indicant que la contrsenya ha estat modificada. 

      - **400 Bad Request**: Si alguna de les dades proporcionades no coincideix amb un usuari de la base de dades. 

      - **405 Method Not Allowed**: Si s'usa un mètode HTTP diferent a POST. 

   Exemple de sol·licitud: 
      .. code-block:: http

         POST /modificar_password/ HTTP/1.1
         Content-Type: application/json

         {
             "nom": "Juan",
             "cognoms": "Pérez",
             "email": "juan.perez@example.com",
             "edat": 30,
             "novaContrasenya": "nueva_password123"
         }

   Exemple de resposta (200 OK):
      .. code-block:: json

         {
             "message": "Contrasenya modificada correctament."
         }

   Exemple de resposta (400 Bad Request):
      .. code-block:: json

         {
             "error": "Algunes dades no són correctes."
         }

   Notas:
      - La nova contrasenya s'emmagatzema de forma encriptada usant la funció:func:`django.contrib.auth.hashers.make_password`.


logout_view
===========

Vista per a tancar la sessió d'usuari invalidant la token de la sessió. 

.. function:: logout_view(request)

   Aquesta vista permet als usuaris tancar la sessió eliminant el token de sessió actiu. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda per el servidor. 

   Mètodes HTTP:
      - **POST**: Aquest és l'únic mètode permès. Processa la sol·licitud per tal de tancar la sessió de l'usuari. 

   Entrades (POST):
      La sol·licitud ha d'incloure un cos JSON amb el següent camp: 
      
      - **token** (str): Token de sessió actual de l'usuari que desitja tancar la sessió. 

   Respostes:
      - **200 OK**: Si el token de sessió és vàlid i s'ha tancat la sessió correctament. 
      
        El cos de la resposta inclou: 
          - **message** (str): Missatge indicant que la sessió s'ha tancat correctament. 

      - **400 Bad Request**: Si el cos de la so·licitud conté dades invàlides o no es pot processar. 
  
      - **404 Not Found**: Si el token de sessió proporcionat no es correspón amb el de cap usuari. 

      - **405 Method Not Allowed**: Si s'usa un mètode HTTP diferent a POST. 

   Exemple de solicitud:
      .. code-block:: http

         POST /logout_view/ HTTP/1.1
         Content-Type: application/json

         {
             "token": "abcd1234efgh5678ijkl9012mnop3456"
         }

   Exemple de resposta (200 OK):
      .. code-block:: json

         {
             "message": "Sessió tancada correctament."
         }

   Exemple de resposta (404 Not Found):
      .. code-block:: json

         {
             "error": "Token de sessió no vàlid."
         }

   Exemple de resposta (400 Bad Request):
      .. code-block:: json

         {
             "error": "Sol·licitud invàlida."
         }



crear_torneig
=============

Vista per a crear un torneig (lliga o eliminatòria) i generar les partides corresponents. 

.. function:: crear_torneig(request)

   Aquesta vista permet a un administrador crear una nova lliga o torneig eliminatori amb una llista de jugadors i generar les partides corresponents. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda per el servidor. 

   Mètodes HTTP:
      - **POST**: Aquest és l'únic mètode permès. Processa la sol·licitud per a crear un torneig. 

   Entrades (POST):
      La sol·licitud ha d'incloure un cos JSON amb els següents camps: 

      - **nomLliga** (str): Nom de la lliga o torneig. 
      - **dataInici** (str): Data d'inici del torneig (en format ISO 8601).
      - **dataFi** (str): Data de finalització del torneig (en format ISO 8601).
      - **tipusTorneig** (str): Tipología de torneig. Pot ser `"Lliga"` o `"TorneigEliminatori"`.
      - **llistaJugadors** (list): Llista dels ojbectes que contenen els IDs dels jugadors participants. Exemple: `[{"id": 1}, {"id": 2}]`.
      - **usuari** (int): ID de l'usuari que sol·licita la creació del torneig (ha de ser un usuari administrador).

   Respostes:
      - **201 Created**: Si el torneig i les partides s'han creat correctament.
      
        El cos de la resposta inclou:
          - **message** (str): Missatge indicant que el torneig i les partides s'han generat amb èxit.

      - **400 Bad Request**: Si les dades proporcionades no son vàlides.

      - **403 Forbidden**: Si l'usuari que realitza la sol·licitud no és administrador. 

      - **404 Not Found**: Si l'usuari administrador o aglún jugador de la llista no existeix. 

      - **405 Method Not Allowed**: Si s'usa un mètode HTTP diferent a POST.

   Exemple de sol·licitud:
      .. code-block:: http

         POST /crear_torneig/ HTTP/1.1
         Content-Type: application/json

         {
             "nomLliga": "Torneig d'Hivern",
             "dataInici": "2024-12-01",
             "dataFi": "2024-12-31",
             "tipusTorneig": "Lliga",
             "llistaJugadors": [
                 {"id": 1},
                 {"id": 2},
                 {"id": 3}
             ],
             "usuari": 1
         }

   Exemple de resposta (201 Created):
      .. code-block:: json

         {
             "message": "Lliga creada amb èxit i partides generades!"
         }

   Exemple de resposta (403 Forbidden):
      .. code-block:: json

         {
             "error": "El jugador no es administrador"
         }

   Exemple de resposta (400 Bad Request):
      .. code-block:: json

         {
             "error": "Invalid JSON data"
         }



getUser_view
============

Vista per a obtenir la informació detallada d'un jugador, inclòs les lligues en les que participa i les partides en les que està involucrat. 

.. function:: getUser_view(request, jugador_id)

   Aquesta vista retorna informació sobre un jugador específic, les seves lligues i partides. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista. 

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda per el servidor. 
      - **jugador_id** (int): L'identificador únic del jugador que es vol consultar. 

   Mètodes HTTP:
      - **GET**: Recupera les dades del jugador. 

   Respostes:
      - **200 OK**: Si es troba el jugador, la resposta inclourà: 

        - **id** (int): Identificador del jugador.
        - **nom** (str): Nom del jugador.
        - **cognoms** (str): Cognoms del jugador.
        - **edat** (int): Edat del jugador.
        - **email** (str): Correu electrònic del jugador.
        - **num_federat** (str): Número de federat.
        - **admin** (bool): Indica si el jugador és administrador.
        - **puntuacioLliga** (int): Puntuació del jugador a la liga.
        - **lligues** (list): Llista de les lligues en les quals participa el jugador, amb:
          - **lliga_id** (int): Identificador de la lliga.
          - **nomLliga** (str): Nom de la lliga.
          - **tipus_torneig** (str): Tipología de torneig.
        - **partides** (list): Llista de partides en les quals participa el jugador, amb:
          - **partida_id** (int): Identificador de la partida.
          - **contrincant** (dict): Informació del contrincant:
            - **id** (int): ID del contrincant.
            - **nom** (str): Nom del contrincant.
            - **cognoms** (str): Cognoms del contrincant.
          - **resultat** (str): Resultat de la partida, o "Pendent" si no s'ha jugat.  

      - **404 Not Found**: Si no es troba un jugador amb el `jugador_id` proporcionat.

   Exemple de solicitud:
      .. code-block:: http

         GET /getUser_view/1/ HTTP/1.1

   Exemple de resposta (200 OK):
      .. code-block:: json

         {
             "id": 1,
             "nom": "Joan",
             "cognoms": "Garcia",
             "edat": 25,
             "email": "joan.garcia@example.com",
             "num_federat": "123456",
             "admin": false,
             "puntuacioLliga": 1200,
             "lligues": [
                 {
                     "lliga_id": 10,
                     "nomLliga": "Lliga d'Hivern",
                     "tipus_torneig": "Lliga"
                 }
             ],
             "partides": [
                 {
                     "partida_id": 5,
                     "contrincant": {
                         "id": 2,
                         "nom": "Maria",
                         "cognoms": "Lopez"
                     },
                     "resultat": "Pendiente"
                 }
             ]
         }

   Exemple de resposta (404 Not Found):
      .. code-block:: json

         {
             "error": "Jugador no trobat."
         }

 
getPartides
===========

Vista per a obtenir la llista de totes les partides registrades al sistema. 

.. function:: getPartides(request)

   Aquesta vista retorna un llistat de totes les partides, incloent informació sobre els jugadors, la lliga sel·leccionada i el resultat. 

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista.

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda per el servidor .

   Mètodes HTTP:
      - **GET**: Recupera la llista de totes les partides. 

   Respostes:
      - **200 OK**: Retorna un llistat amb les partides, en la qual cada element inclou: 
        
        - **lliga** (str): Nom de la lliga associada a la partida. 
        - **partida_pk** (int): Id de la partida. 
        - **jugador1** (str): Nom del primer jugador
        - **jugador1_pk** (int): Id del primer jugador. 
        - **jugador2** (str): Nom del segon jugador
        - **jugador2_pk** (int): ID del segon jugador.
        - **resultat** (str): Resultat de la partida (pot ser `null` si està pendent).

   Exemple de sol·licitud: 
      .. code-block:: http

         GET /getPartides/ HTTP/1.1

   Exemple de resposta (200 OK):
      .. code-block:: json

         [
             {
                 "lliga": "Lliga d'Hivern",
                 "partida_pk": 1,
                 "jugador1": "Joan",
                 "jugador1_pk": 1,
                 "jugador2": "Maria",
                 "jugador2_pk": 2,
                 "resultat": null
             },
             {
                 "lliga": "Torneig de Primavera",
                 "partida_pk": 2,
                 "jugador1": "Albert",
                 "jugador1_pk": 3,
                 "jugador2": "Clara",
                 "jugador2_pk": 4,
                 "resultat": "Jugador1 Guanya"
             }
         ]

   Notes:
      - La resposta és una llista d'objectes JSON en el qual cada objecte respón a una partida. 
      - Si no hi ha cap partida registrada, es retorna una llista buida (`[]`).
      - El camp **resultat** serà `null` si el resultat de la partida no està definit. 

getLligues
==========

Vista per obtenir el llistat de totes les lligues registrades al sistema.

.. function:: getLligues(request)

   Aquesta vista retorna una llista de totes les lligues amb la seva informació bàsica.

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista.

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda pel servidor.

   Mètodes HTTP:
      - **GET**: Recupera el llistat de totes les lligues.

   Respostes:
      - **200 OK**: Retorna una llista amb les lligues registrades, on cada element inclou:

        - **lliga_pk** (int): Identificador únic de la lliga.
        - **nom_lliga** (str): Nom de la lliga.

   Exemple de sol·licitud:
      .. code-block:: http

         GET /getLligues/ HTTP/1.1

   Exemple de resposta (200 OK):
      .. code-block:: json

         [
             {
                 "lliga_pk": 1,
                 "nom_lliga": "Lliga d'Hivern"
             },
             {
                 "lliga_pk": 2,
                 "nom_lliga": "Torneig de Primavera"
             }
         ]

   Notes:
      - La resposta és una llista d'objectes JSON on cada objecte representa una lliga.
      - Si no hi ha lligues registrades, es retorna una llista buida (`[]`).
      - Aquesta vista només inclou informació bàsica sobre les lligues per minimitzar la càrrega de dades.

registrarResultatPartida
=========================

Vista per registrar el resultat d'una partida.

.. function:: registrarResultatPartida(request)

   Aquesta vista permet registrar el resultat d'una partida i actualitzar la puntuació de la lliga associada.

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista.

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda pel servidor.

   Mètodes HTTP:
      - **POST**: Registra el resultat d'una partida.

   Entrada JSON:
      - **partida_pk** (int, obligatori): Identificador de la partida.
      - **guanyador** (str, obligatori): Indica el guanyador de la partida. Valors possibles:
         - `"jugador1"`: Guanya el jugador 1.
         - `"jugador2"`: Guanya el jugador 2.
         - `"EMP"`: Partida empatada.

   Respostes:
      - **201 Created**: Resultat registrat correctament.
      - **400 Bad Request**: Dades d'entrada no vàlides o error amb el guanyador especificat.
      - **404 Not Found**: Partida o jugador no trobats.
      - **405 Method Not Allowed**: Intent d'actualitzar una partida que ja té un resultat registrat.

   Exemple de sol·licitud:
      .. code-block:: http

         POST /registrarResultatPartida/ HTTP/1.1
         Content-Type: application/json

         {
             "partida_pk": 1,
             "guanyador": "jugador1"
         }

   Exemple de resposta (201 Created):
      .. code-block:: json

         {
             "message": "S'ha desat el resultat amb èxit!"
         }

   Exemple de resposta (404 Not Found):
      .. code-block:: json

         {
             "error": "Partida no trobada"
         }

   Exemple de resposta (400 Bad Request):
      .. code-block:: json

         {
             "error": "Guanyador no vàlid"
         }

   Notes:
      - Si totes les partides d'una lliga tenen resultats registrats, el jugador amb més punts es considera el guanyador de la lliga.
      - El camp **resultat** de la partida pot tenir els valors:
         - `"VJ1"`: Guanya el jugador 1.
         - `"VJ2"`: Guanya el jugador 2.
         - `"EMP"`: Partida empatada.
      - Si ja hi ha un resultat per a la partida, no es permet registrar-ne un de nou.

buscar_jugador
==============

Vista per buscar jugadors pel seu nom.

.. function:: buscar_jugador(request)

   Aquesta vista permet buscar jugadors que coincideixin parcialment amb un nom especificat com a paràmetre de consulta.

   Decoradors:
      - :decorator:`@csrf_exempt`: Desactiva la protecció CSRF per a aquesta vista.

   Paràmetres:
      - **request** (:class:`django.http.HttpRequest`): La sol·licitud HTTP rebuda pel servidor.

   Mètodes HTTP:
      - **GET**: Cerca jugadors pel nom.

   Paràmetres de consulta:
      - **nom** (str, opcional): Nom o part del nom del jugador que es vol buscar. La cerca no és sensible a majúscules/minúscules.

   Respostes:
      - **200 OK**: Retorna una llista de jugadors que coincideixen amb la cerca. Cada element inclou:
         - **id** (int): Identificador únic del jugador.
         - **nom** (str): Nom del jugador.
         - **cognoms** (str): Cognoms del jugador.

      - **[]**: Si no es proporciona cap nom o no hi ha coincidències.

   Exemple de sol·licitud:
      .. code-block:: http

         GET /buscar_jugador/?nom=Joan HTTP/1.1

   Exemple de resposta (200 OK):
      .. code-block:: json

         [
             {
                 "id": 1,
                 "nom": "Joan",
                 "cognoms": "Garcia"
             },
             {
                 "id": 2,
                 "nom": "Joan",
                 "cognoms": "Martínez"
             }
         ]

   Exemple de resposta amb cap resultat:
      .. code-block:: json

         []

   Notes:
      - Si no es proporciona el paràmetre **nom**, la resposta serà una llista buida.
      - La cerca utilitza l'operador `icontains`, que permet buscar coincidències parcials sense distingir majúscules/minúscules.
      - Aquesta vista retorna únicament informació bàsica dels jugadors. Per obtenir més detalls, cal utilitzar altres vistes.

getResultatsLliga
=================

.. function:: getResultatsLliga(request)

   Aquesta funció permet obtenir els resultats d'una lliga específica, retornant les dades de les partides associades.

   **Decoradors**:
      - ``@csrf_exempt``

   **Mètodes acceptats**:
      - GET

   **Paràmetres**:

      - ``lliga_id`` (*str*): Identificador únic de la lliga que es vol consultar. S'ha d'incloure com a paràmetre GET.

   **Retorn**:

      - Si la lliga existeix:
         - Tipus: ``JsonResponse``
         - Contingut: Llista de diccionaris amb informació de les partides de la lliga. Cada element conté:
            - ``partida_id`` (*int*): Identificador de la partida.
            - ``jugador1`` (*str*): Nom del primer jugador.
            - ``jugador2`` (*str*): Nom del segon jugador.
            - ``resultat`` (*str*): Resultat de la partida, o "Pendent" si encara no està definit.

      - Si la lliga no existeix:
         - Tipus: ``JsonResponse``
         - Contingut: Diccionari amb l'error següent:
            - ``error`` (*str*): Missatge indicant que la lliga no ha estat trobada.
         - Codi HTTP: ``404``

   **Exemples**:

   *Consulta exitosa:*

   .. code-block:: http

      GET /getResultatsLliga?lliga_id=1 HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 200 OK
      Content-Type: application/json

      [
         {
            "partida_id": 1,
            "jugador1": "Anna",
            "jugador2": "Pere",
            "resultat": "3-2"
         },
         {
            "partida_id": 2,
            "jugador1": "Joan",
            "jugador2": "Carla",
            "resultat": "Pendent"
         }
      ]

   *Error: Lliga no trobada:*

   .. code-block:: http

      GET /getResultatsLliga?lliga_id=999 HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 404 Not Found
      Content-Type: application/json

      {
         "error": "Lliga no trobada."
      }


get_ranking
===========

.. function:: get_ranking(request)

   Aquesta funció retorna el rànquing de jugadors, ordenats per puntuació de forma descendent.

   **Decoradors**:
      - ``@csrf_exempt``

   **Mètodes acceptats**:
      - GET

   **Retorn**:

      - Tipus: ``JsonResponse``
      - Contingut: Una llista de diccionaris, on cada element representa un jugador. Els camps inclosos són:
         - ``id`` (*int*): Identificador únic del jugador.
         - ``nom`` (*str*): Nom del jugador.
         - ``cognoms`` (*str*): Cognoms del jugador.
         - ``puntuacio`` (*int*): Puntuació total del jugador.

   **Exemples**:

   *Consulta exitosa:*

   .. code-block:: http

      GET /get_ranking HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 200 OK
      Content-Type: application/json

      [
         {
            "id": 1,
            "nom": "Anna",
            "cognoms": "Martínez",
            "puntuacio": 1500
         },
         {
            "id": 2,
            "nom": "Joan",
            "cognoms": "García",
            "puntuacio": 1400
         },
         {
            "id": 3,
            "nom": "Carla",
            "cognoms": "López",
            "puntuacio": 1300
         }
      ]

   **Notes**:
      - Els jugadors sense puntuació seran inclosos al final del rànquing amb un valor de puntuació nul o zero, segons el model de dades.
      - Aquesta vista no requereix paràmetres d'entrada.


get_classificacioLliga
=======================

.. function:: get_classificacioLliga(request)

   Aquesta funció retorna la classificació dels jugadors associats a una lliga específica, ordenats per puntuació dins de la lliga.

   **Decoradors**:
      - ``@csrf_exempt``

   **Mètodes acceptats**:
      - GET

   **Paràmetres**:

      - ``lliga_Nom`` (*str*): Nom de la lliga. És obligatori passar aquest paràmetre com a part de la consulta GET.

   **Retorn**:

      - Si la lliga existeix:
         - Tipus: ``JsonResponse``
         - Contingut: Una llista de diccionaris, on cada element representa un jugador de la lliga. Els camps inclosos són:
            - ``id`` (*int*): Identificador únic del jugador.
            - ``nom`` (*str*): Nom del jugador.
            - ``cognoms`` (*str*): Cognoms del jugador.
            - ``puntuacioLliga`` (*int*): Puntuació del jugador dins de la lliga.

      - Si falta el paràmetre ``lliga_Nom``:
         - Tipus: ``JsonResponse``
         - Contingut: Diccionari amb l'error següent:
            - ``error`` (*str*): Missatge indicant que falta el paràmetre.
         - Codi HTTP: ``400``

      - Si la lliga no existeix:
         - Tipus: ``JsonResponse``
         - Contingut: Diccionari amb l'error següent:
            - ``error`` (*str*): Missatge indicant que la lliga no ha estat trobada.
         - Codi HTTP: ``404``

      - Si es fa servir un mètode no permès:
         - Tipus: ``JsonResponse``
         - Contingut: Diccionari amb l'error següent:
            - ``error`` (*str*): Missatge indicant que el mètode no està permès.
         - Codi HTTP: ``405``

   **Exemples**:

   *Consulta exitosa:*

   .. code-block:: http

      GET /get_classificacioLliga?lliga_Nom=Lliga1 HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 200 OK
      Content-Type: application/json

      [
         {
            "id": 1,
            "nom": "Anna",
            "cognoms": "Martínez",
            "puntuacioLliga": 150
         },
         {
            "id": 2,
            "nom": "Joan",
            "cognoms": "García",
            "puntuacioLliga": 140
         },
         {
            "id": 3,
            "nom": "Carla",
            "cognoms": "López",
            "puntuacioLliga": 130
         }
      ]

   *Error: Falta el paràmetre ``lliga_Nom``:*

   .. code-block:: http

      GET /get_classificacioLliga HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 400 Bad Request
      Content-Type: application/json

      {
         "error": "Especifica un ID o nom de la lliga"
      }

   *Error: Lliga no trobada:*

   .. code-block:: http

      GET /get_classificacioLliga?lliga_Nom=LligaInexistent HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 404 Not Found
      Content-Type: application/json

      {
         "error": "Lliga no trobada"
      }

   *Error: Mètode no permès:*

   .. code-block:: http

      POST /get_classificacioLliga HTTP/1.1
      Host: example.com

      Resposta:
      HTTP/1.1 405 Method Not Allowed
      Content-Type: application/json

      {
         "error": "Método no permitido"
      }
