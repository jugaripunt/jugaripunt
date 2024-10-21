<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-cover">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h1 class="text-3xl font-bold mb-8 text-center">
        Iniciar Sessió
      </h1>
      <form @submit.prevent="submit">
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
        <button
          class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4"
          type="submit"
        >
          Iniciar Sessió
        </button>
      </form>
      <div class="flex flex-col space-y-4">
        <button
          class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-700 w-full"
          @click="loginWithGoogle"
        >
          Iniciar Sessió amb Google
        </button>
        <button
          class="bg-blue-800 text-white py-2 px-4 rounded hover:bg-blue-900 w-full"
          @click="loginWithFacebook"
        >
          Iniciar Sessió amb Facebook
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async submit () {
      try {
        //const baseURL = process.env.API_BASE_URL || 'http://localhost:3000'
        const baseURL = process.env.API_BASE_URL
        await axios.post(`api/jugador/login`, {
          method: 'POST',
          headers: {
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          },
          email: this.email,
          password: this.password
        })
      } catch (error) {
        console.error('Error logging in:', error)
      }
    },
    loginWithGoogle () {
      // Implement Google login
    },
    loginWithFacebook () {
      // Implement Facebook login
    }
  }
}
</script>

<style scoped>
</style>
