<template>
  <div id="app">
    <Header> </Header>
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';
import Movie from '@/components/Movie.vue';
import Movie2 from '@/components/Movie2.vue';

export default {
  name: 'App',
  components: {
    Header,
    Movie,
    Movie2
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
  --accent-yellow: #e6d054;
  
  /* Text Colors */
  --text-light: #FAFAFF;
}

body {
  font-family: 'Source Code Pro', monospace;
  padding: 0.2em;
  background-color: var(--secondary-dark);
  letter-spacing: 0.05rem;
  color: var(--text-light);
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;
  zoom: 90%;
}
body::-webkit-scrollbar {
    display: none;
}
h2 {
  font-family: rubik, sans-serif;
  color: var(--text-light);
}
a {
  text-decoration: none;
  color: var(--text-light);
}
</style>