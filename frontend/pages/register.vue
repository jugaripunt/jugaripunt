<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-cover">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h1 class="text-3xl font-bold mb-8 text-center">
        Alta de nou usuari
      </h1>
      <form id="formulariregistre" @submit.prevent="submit">
        <div class="mb-4">
          <label class="block text-gray-700" for="email">Email</label>
          <input
            id="email"
            v-model="email"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="email"
            required
            placeholder="Email"
          >
        </div>
        <div class="mb-4">
          <label class="block text-gray-700" for="password">Contrasenya</label>
          <input
            id="password"
            v-model="password"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="password"
            required
            placeholder="Contrasenya"
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="passwordRepeat">Repeteix contrasenya</label>
          <input
            id="passwordRepeat"
            v-model="passwordRepeat"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="password"
            required
            placeholder="Repeteix contrasenya"
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="nom">Nom</label>
          <input
            id="nom"
            v-model="nom"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="text"
            required
            placeholder="Nom"
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="cognoms">Cognoms</label>
          <input
            id="cognoms"
            v-model="cognoms"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="text"
            required
            placeholder="Cognoms"
          >
        </div>

        <div class="mb-4">
          <label class="block text-gray-700" for="edat">Edat</label>
          <input
            id="edat"
            v-model="edat"
            class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
            type="number"
            required
            placeholder="Edat"
          >
        </div>

        <button
          class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4"
          type="submit"
        >
          Registre d'usuari
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
      email: '',
      password: '',
      passwordRepeat: '',
      nom: '',
      cognoms: '',
      edat: ''
    }
  },
  methods: {
    async submit () {
      
      if (this.password !== this.passwordRepeat) {
        alert('Les contrasenyes no coincideixen. Si us plau, intenta-ho de nou.')
        return
      }

      try {
        
        //const baseURL = process.env.API_BASE_URL || 'http://localhost:3000'
        const response = await axios.post(`api/jugador/`, {
          email: this.email,
          contrasenya: this.password,
          nom: this.nom,
          cognoms: this.cognoms,
          edat: this.edat
        })

        if (response.status === 201) {
          alert('Jugador registrat amb èxit!')
          document.getElementById('formulariregistre').reset()
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
