Model Documentation
====================

Documentació dels models utilitzats a l'aplicació. 

.. module:: your_module_name
   :synopsis: Brief description of the module

Model: Jugador
---------------------

**Description**

Model per a la representació d'un jugador. 

**Attributes**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - `id`
     - Identificador únic per a cada jugador
   * - `nom`
     - Nom del jugador
   * - `cognoms`
     - Cognoms del jugador
   * - `edat`
     - Edat del jugador
   * - `email`
     - Correu electrònic del jugador (format de correu electrònic)
   * - `contrasenya`
     - Contrasenya del jugador
   * - `session_token`
     - Camp opcional per al token de la sessió
   * - `admin`
     - S'utilitza per a controlar si és administrador o no
   * - `num_federat`
     - Número de federat del jugador

Model: Lliga
---------------------

**Description**

Model per a la representació de la lliga. 

**Attributes**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - `nomLliga`
     - Nom de la lliga
   * - `dataInici`
     - Data d'inici de la lliga
   * - `dataFi`
     - Data de finalització de la lliga
   * - `tipusTorneig`
     - Lliga o torneig
   * - `usuariAdmin`
     - Identificador únic de l'usuari que administra la lliga. 
   * - `llistaJugadors`
     - Relació dels jugadors que formen part de la lliga
   * - `resultat`
     - Identificador únic del guanyador de la lliga

Model: Partida
---------------------

**Description**

Model per a la representació de la partida. 

**Attributes**

.. list-table::
   :widths: 20 80
   :header-rows: 1

   * - Attribute
     - Description
   * - `lliga`
     - Identificador únic de la lliga de la qual forma part la partida
   * - `jugador1`
     - Jugador de la partida
   * - `jugador2`
     - jugador de la partida
   * - `resultat`
     - Resultat de la partida: guanya gujador 1, guanya jugador 2, empat
