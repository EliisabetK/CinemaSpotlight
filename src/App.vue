<template>
 <Background>
    <div id="app">
      <Header></Header>
      <router-view/>
    </div>
</Background>    

</template>

<script>
import Header from '@/components/Header.vue';
import Movie from '@/components/Movie.vue';
import Movie2 from '@/components/Movie2.vue';
import Background from '@/components/Background.vue';
import formatDate from '@/mixins/formatDate.js';

export default {
  name: 'App',
  mixins: [formatDate],
  components: {
    Header,
    Movie,
    Movie2,
    Background
  },
  mounted() {
    var video = document.getElementById('vid');
    if (video) {
      video.playbackRate = 0.5;
    }
  },
  methods: {
    formatDate(dateString) {
        const releasedate = new Date(dateString);
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return releasedate.toLocaleDateString(undefined, options);
      },
  }
};
</script>

<style>

:root {
  /* Primary Colors */
  --primary-color: #2d2d2f;
  --primary-dark: #1f2022;
  --primary-hover: #46464a;
  
  /* Secondary Colors */
  --secondary-color: #95979F;
  --secondary-dark: #000000;
  
  /* Background Colors */
  --accent-light: #acd3ec;
  --accent-dark: #81b0f7;
  --accent-yellow: #e6d054;
  --accent-yellow-hover: rgb(255, 236, 128);

  
  /* Text Colors */
  --text-light: #FAFAFF;
  --text-dark: #1e1e2b;

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
  margin: 0;
}
body::-webkit-scrollbar {
    display: none;
}
h2 {
  font-family: rubik, sans-serif;
  color: var(--text-light);
}
h3 {
  font-family: rubik, sans-serif;
  color: var(--text-light);
}
a {
  text-decoration: none;
  color: var(--text-light);
}
.video-background {
  position: absolute; /* Absolute position */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1; /* Place it behind other elements */
}

.video-background video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1; /* Place it behind other elements */
}


</style>