<template>
  <div id="app">
    <Header> </Header>
    <router-view/>
    <Footer></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Movie from '@/components/Movie.vue';

export default {
  name: 'App',
  components: {
    Header,
    Movie
  },
};
</script>

// General style of the app
<style>

:root {
  /* Primary Colors */
  --primary-color: #313f79;
  --primary-dark: #1E2749;
  
  /* Secondary Colors */
  --secondary-color: #95979F;
  --secondary-dark: #30343F;
  
  /* Background Colors */
  --accent-light: #E4D9FF;
  --accent-dark: #8687B4;
  
  /* Text Colors */
  --text-light: #FAFAFF;
}

body {
  font-family: monospace, sans-serif;
  margin: 0;
  padding: 0.2em;
  background-color: var(--secondary-dark);
}

</style>