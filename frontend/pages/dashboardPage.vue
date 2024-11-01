<template>
  <div class="flex flex-col">
    <section class="bg-gray-100 p-8 shadow-lg min-h-screen w-full max-w-7xl pl-4">
      <h1 class="text-4xl mt-4 mb-8">
        Benvingut <b>{{ nomUsuari }}</b>
      </h1>
      <p class="text-xl mb-8">
         Aquest és el dashboard de la zona privada de Juga i Punt. Proximament accedeix aqui als tornejos.

        a la part superior veureu el menú amb totes les opcions i ja no s'ha de mostrar ni login ni registre perque ja estás conectat.
      </p>
    </section>
  </div>
</template>

<script>
export default {
  name: 'DashboardPage',
  data () {
    return {
      nomUsuari: null,
    }
  },
  mounted () {
    this.getUserName()
  },
  methods: {
    getUserName () {
      this.nomUsuari = 'anònim' // TO - DO Axios endpoint amb el nom usuari
    }
  }
}
</script>

<style scoped>
</style>
