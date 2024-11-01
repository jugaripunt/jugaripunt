<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-cover">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h1 class="text-3xl font-bold mb-8 text-center">
        Cerca de Jugador
      </h1>
      <form @submit.prevent>
        <div class="mb-4">
          <label class="block text-gray-700" for="nombreJugador">Nom del Jugador</label>
          <input
            id="nombreJugador"
            v-model="nomJugador"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="text"
            placeholder="Escriu el nom del jugador"
            @input="buscarJugador"
          >
        </div>
      </form>

      <!-- Resultados de búsqueda -->
      <div v-if="resultats.length" class="mt-4">
        <h2 class="text-lg font-semibold">
          Resultats de la cerca:
        </h2>
        <ul class="mt-2">
          <li
            v-for="jugador in resultats"
            :key="jugador.id"
            class="border-b border-gray-300 py-2 cursor-pointer hover:bg-gray-200"
            @click="seleccionarJugador(jugador)"
          >
            {{ jugador.nom }} {{ jugador.cognoms }}
          </li>
        </ul>
      </div>

      <!-- Botó Afegir Jugador -->
      <button
        class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4 mt-4"
        :disabled="!jugadorSeleccionat"
        @click="afegirJugador"
      >
        Afegir Jugador
      </button>

      <!-- Llista de jugadors afegits -->
      <div v-if="jugadorsAfegits.length" class="mt-4">
        <h2 class="text-lg font-semibold">
          Jugadors Afegits:
        </h2>
        <ul class="mt-2">
          <li
            v-for="jugador in jugadorsAfegits"
            :key="jugador.id"
            class="border-b border-gray-300 py-2"
          >
            {{ jugador.nom }} {{ jugador.cognoms }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      nomJugador: '',
      resultats: [],
      jugadorSeleccionat: null,
      jugadorsAfegits: [],
      numJugadors: 0 // Inicializa numJugadors
    }
  },
  mounted () {
    // Mostrar el número de jugadores recibido desde CrearLliga
    this.numJugadors = this.$route.query.numJugadors
    console.log('Número de Jugadores recibido:', this.numJugadors)
  },

  methods: {
    async buscarJugador () {
      // Si el camp de busqueda està buit neteja els resultats
      if (!this.nomJugador) {
        this.resultats = []
        return
      }

      try {
        const baseURL = process.env.API_BASE_URL || 'http://localhost:8000'
        const response = await axios.get(`${baseURL}/api/jugador/buscar`, {
          params: { nom: this.nomJugador } // envia el nom com a paràmetre
        })

        this.resultats = response.data // Actualitza els resultats amb les dades de la resposta
      } catch (error) {
        console.error('Error en la cerca:', error)
      }
    },
    seleccionarJugador (jugador) {
      this.jugadorSeleccionat = jugador
    },
    async afegirJugador () {
      if (!this.jugadorSeleccionat) { return }

      try {
        const baseURL = process.env.API_BASE_URL || 'http://localhost:8000'
        await axios.post(`${baseURL}/api/lliga/afegir_jugador`, this.jugadorSeleccionat)

        // Afegir el jugador seleccionat a la llista local de jugadors afegits
        this.jugadorsAfegits.push(this.jugadorSeleccionat)

        // envia la llista de jugadors al backend, si aquesta ja es igual al numero de jugadors de la lliga
        if (this.jugadorsAfegits.length === parseInt(this.numJugadors)) {
          await axios.post(`${baseURL}/api/torneig/afegir_jugadors`, this.jugadorsAfegits)
          console.log('Jugadors afegits:', this.jugadorsAfegits)
        }
        // neteja la selecció i el camp de búsqueda
        this.jugadorSeleccionat = null
        this.nomJugador = ''
        this.resultats = []
      } catch (error) {
        console.error('Error al afegir el jugador:', error)
      }
    }
  }
}
</script>

<style scoped>
</style>
