<template>
  <div class="min-h-screen flex flex-col justify-center items-center bg-cover">
      <div class="bg-white p-8 rounded-lg shadow-lg text-center max-w-2xl">
        <h1 class="text-4xl font-bold mb-4">
          Jugar i Punt!
        </h1>
        <p class="text-xl mb-8">
          El teu portal per organitzar i veure tornejos d'escacs
        </p>
        <nuxt-link to="register">
          <button class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700">
            Registra't Ara
          </button>
        </nuxt-link>
      </div>
    </div>
</template>

<script>
export default {
  name: 'HomePage',
  data () {
    return {
      //isAuthenticated: false
    }
  },
  mounted () {
    //this.checkAuthentication()
  },
  methods: {
    checkAuthentication () {
      // Comprovar si existeix el token a localStorage
      //const token = localStorage.getItem('authToken')
      //this.isAuthenticated = !!token // Assignar true o false segons existeixi el token
    }
  }
}
</script>

<style scoped>
</style>
