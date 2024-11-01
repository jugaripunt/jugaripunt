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
          <!--Botó Menú-->
          <UButton v-if="isAdmin" label="Menú" @click="menuIsOpen = true" />
          <!--Contingut del panell-->
          <USlideover v-model="menuIsOpen" :overlay="false">
            <UCard class="flex flex-col flex-1" :ui="{ body: { base: 'flex-1' }, ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
              <template #header>
                <div class="flex items-center justify-between">
                  <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
                    Opcions de la plataforma
                  </h3>
                  <UButton color="gray" variant="ghost" icon="i-heroicons-x-mark-20-solid" class="-my-1" @click="menuIsOpen = false" />
                </div>
              </template>

              <Placeholder class="h-full" />

              <div class="flex flex-col gap-2">
                <nuxt-link to="/dashboardPage">
                  <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Dashboard
                  </button>
                </nuxt-link>
                <nuxt-link to="/profile">
                  <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Perfil
                  </button>
                </nuxt-link>
                <nuxt-link to="/estadistiques">
                  <button class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Estadístiques
                  </button>
                </nuxt-link>
                <!--Button crear lliga-->
                <nuxt-link to="/crearlliga">
                  <button v-if="isAdmin" class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Crear lliga
                  </button>
                  <button v-if="!isAdmin" class="w-full bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-700" disabled>
                    Crear lliga
                  </button>
                </nuxt-link>
                <!--Button resultat partides-->
                <nuxt-link to="/ResultatsPartides">
                  <button v-if="isAdmin" class="w-full bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Resultats partides
                  </button>
                  <button v-if="!isAdmin" class="w-full bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-700" disabled>
                    Resultats partides
                  </button>
                </nuxt-link>
                <button
                  class="w-full bg-red-500 text-white py-2 px-4 rounded hover:bg-red-700"
                  @click="logout"
                >
                  Logout
                </button>
              </div>
            </UCard>
          </USlideover>
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
      isAuthenticated: false, // Estat per verificar si l'usuari està autenticat
      isAdmin: true, // Estar per verificar si l'usuari és admin
      menuIsOpen: false
    }
  },
  mounted () {
    this.checkAuthentication() // Comprova l'autenticació en muntar el component
    // this.checkIsAdmin()
  },
  methods: {
    checkAuthentication () {
      // Comprovar si existeix el token a localStorage
      const token = localStorage.getItem('authToken')
      this.isAuthenticated = !!token // Assignar true o false segons existeixi el token
    },
    checkIsAdmin () {
      // Comprovar si l'usari és admin
      // this.isAdmin = false // TO DO -- obtenir dades de l'endpoint
      // const baseURL = process.env.API_BASE_URL || 'http://localhost:8000'
      try {
        // const response = axios.get(`${baseURL}/api/jugador/dades/`) // TO-DO. Acabar de concretar quin és l'endpoint
      } catch (error) {
        console.log(error)
      }
    },
    async logout () {
      try {
        const token = localStorage.getItem('authToken') // Obtenir el token del localStorage
        const baseURL = process.env.API_BASE_URL || 'http://localhost:8000'

        // Enviar el token en el cos de la sol·licitud
        await axios.post(`${baseURL}/api/logout`, { token })

        // Eliminar el token de localStorage
        localStorage.removeItem('authToken')

        // Actualitzar l'estat
        this.isAuthenticated = false

        // Redirigir a la pàgina d'inici de sessió
        this.$router.push('/login')
      } catch (error) {
        console.error('Error logging out:', error)
      }
    }
  }
}
</script>

<style scoped>
</style>
