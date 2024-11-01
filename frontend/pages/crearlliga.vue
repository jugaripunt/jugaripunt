<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-cover">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h1 class="text-3xl font-bold mb-8 text-center">
        Registre de Lliga o Torneig
      </h1>
      <form id="formulariTorneig" @submit.prevent="submit">
        <div class="mb-4">
          <label class="block text-gray-700" for="nomLliga">Nom de la Lliga</label>
          <input
            id="nomLliga"
            v-model="nomLliga"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="text"
            required
            placeholder="Nom de la lliga"
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="dataInici">Data d'Inici</label>
          <input
            id="dataInici"
            v-model="dataInici"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="date"
            required
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="dataFi">Data de Fi</label>
          <input
            id="dataFi"
            v-model="dataFi"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="date"
            required
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="tipusTorneig">Tipus de Torneig</label>
          <select
            id="tipusTorneig"
            v-model="tipusTorneig"
            class="form-select mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            required
          >
            <option value="">
              Selecciona un tipus
            </option>
            <option value="liga">
              Lliga
            </option>
            <option value="torneigEliminatori">
              Torneig Eliminatori
            </option>
          </select>
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="numJugadors">Número de Jugadors</label>
          <input
            id="numJugadors"
            v-model="numJugadors"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="number"
            required
            placeholder="Número de jugadors"
          >
        </div>

        <button
          class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4"
          type="submit"
        >
          Registrar Lliga/Torneig
        </button>
      </form>
    </div>
  </div>
</template>

<script>

import axios from 'axios'

export default {
  data () {
    return {
      nomLliga: '',
      dataInici: '',
      dataFi: '',
      tipusTorneig: '',
      numJugadors: ''
    }
  },
  methods: {
    async submit () {
      try {
        const baseURL = process.env.API_BASE_URL || 'http://localhost:8000'
        const response = await axios.post(`${baseURL}/api/noutorneig`, {
          nomLliga: this.nomLliga,
          dataInici: this.dataInici,
          dataFi: this.dataFi,
          tipusTorneig: this.tipusTorneig,
          numJugadors: this.numJugadors
        })

        if (response.status === 201) {
          alert('Lliga o Torneig registrat amb èxit!')
          document.getElementById('formulariTorneig').reset()
          // Navegar a la pàgina Afegeix Jugador amb el número de jugadors
          this.$router.push(`/afegeixjugadors?numJugadors=${this.numJugadors}`)
        }
      } catch (error) {
        alert(`Error de registre: ${error.response?.data.error || error.message}`)
      }
    }
  }
}
</script>

<style scoped>
</style>
