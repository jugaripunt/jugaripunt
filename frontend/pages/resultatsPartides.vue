<template>
  <div class="min-h-screen flex flex-col justify-center items-center">
    <section class="bg-white p-8 rounded-lg shadow-lg w-full max-w-4xl mt-4">
      <h1 class="text-4xl text-center mt-4 mb-8">
        Formulari per a introduïr els resultats
      </h1>
      <div class="space-y-8">
        <!-- Seccio d'introduccio -->
        <form @submit.prevent="submit">
          <div class="mb-4">
            <label class="block text-gray-700" for="date">Data partida</label>
            <input
              id="date"
              v-model="date"
              class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
              type="date"
              required
              placeholder="Data partida"
            >
          </div>
          <div class="mb-4">
            <label class="block text-gray-700" for="jugador1">Nom jugador 1</label>
            <input
              id="jugador1"
              v-model="jugador1"
              class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
              type="text"
              required
              placeholder="Jugador 1"
            >
          </div>
          <div class="mb-4">
            <label class="block text-gray-700" for="jugador1">Nom jugador 2</label>
            <input
              id="jugador2"
              v-model="jugador1"
              class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
              type="text"
              required
              placeholder="Jugador 2"
            >
          </div>
          <div class="mb-4">
            <label class="block text-gray-700" for="resultat">Resultat</label>
            <input
              id="resultat"
              v-model="resultat"
              class="form-input mt-1 block w-full h-12 rounded px-4 border border-gray-300"
              type="number"
              required
              placeholder="Resultat"
            >
          </div>
          <button
            class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700 w-full mb-4"
            type="submit"
          >
            Enviar resultats
          </button>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: 'ResultatsPartides'
}
</script>

<style scoped>
</style>
