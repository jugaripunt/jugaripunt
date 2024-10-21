<template>
  <header class="p-4 bg-white text-slate-800 dark:bg-slate-800 dark:text-white">
    <div class="container mx-auto flex justify-between items-center">
      <nuxt-link to="/" class="text-2xl font-bold">
        Jugar i Punt!
      </nuxt-link>
      <nav>
        <ul class="flex space-x-4">
          <li>
            <nuxt-link to="/" class="hover:underline">
              Inici
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/about" class="hover:underline">
              Sobre nosaltres
            </nuxt-link>
          </li>
          <li>
            <nuxt-link to="/contact" class="hover:underline">
              Contacte
            </nuxt-link>
          </li>
        </ul>
      </nav>
      <div class="flex space-x-4">
        <template v-if="isAuthenticated">
          <nuxt-link to="/profile">
            <button class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
              Perfil
            </button>
          </nuxt-link>
          <button class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-700" @click="logout">
            Logout
          </button>
        </template>
        <template v-else>
          <nuxt-link to="/register">
            <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700">
              Registre
            </button>
          </nuxt-link>
          <nuxt-link to="/login">
            <button class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-700">
              Iniciar Sessió
            </button>
          </nuxt-link>
        </template>
      </div>
    </div>
  </header>
</template>

<script>
import axios from 'axios'

export default {
  name: 'AppHeader',
  data () {
    return {
      isAuthenticated: false
    }
  },
  created () {
    this.checkAuth()
  },
  methods: {
    async checkAuth () {
      try {
        //const baseURL = process.env.API_BASE_URL || 'http://localhost:3000'
        const response = await axios.get(`api/auth/check`)
        this.isAuthenticated = response.data.isAuthenticated
      } catch (error) {
        console.error('Error checking authentication:', error)
      }
    },
    async logout () {
      try {
        //const baseURL = process.env.API_BASE_URL || 'http://localhost:3000'
        await axios.post(`api/auth/logout`)
        this.isAuthenticated = false
      } catch (error) {
        console.error('Error logging out:', error)
      }
    }
  }
}
</script>

<style scoped>
</style>
