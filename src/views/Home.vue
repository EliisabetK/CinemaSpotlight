<template>
  <div>
    <div class="toggle-container">
      <button class="btn" @click="toggleInCinemas(true)">In cinemas</button>
      <button class="btn" @click="toggleInCinemas(false)">Coming soon</button>
    </div>
    <div class="container">
      <main>
        <Movie
          v-for="movie in filteredMovies"
          :key="movie.id"
          :id="movie.id"
          :photo="movie.photo"
          :name="movie.name"
          :imdb="movie.imdb"
          :letterboxd="movie.letterboxd"
          :rottentomatoes="movie.rottentomatoes"
          :releasedate="movie.releasedate"
        />
      </main>
    </div>
    <div class="container">
      <button @click="scrollToFull" class="arrow">﹀</button>
    </div>
    <div id="full"></div>
  </div>
</template>

<script>
import Movie from "@/components/Movie.vue";
import { scrollTo } from "vue-scrollto";

export default {
  name: "MainView",
  data() {
    return {
      inCinemas: true,
    };
  },
  computed: {
    movieList() {
      return this.$store.state.movieList;
    },
    filteredMovies() {
      const currentDate = new Date();
      if (this.inCinemas) {
        return this.movieList.filter((movie) => new Date(movie.releasedate) <= currentDate);
      } else {
        return this.movieList.filter((movie) => new Date(movie.releasedate) > currentDate);
      }
    },
  },
  components: {
    Movie,
  },
  methods: {
    toggleInCinemas(value) {
      this.inCinemas = value;
    },
    scrollToFull() {
      // Scroll to the element with id 'full' with a smooth animation
      scrollTo("#full", 800);
    },
  },
  mounted() {
    this.$store.dispatch("fetchMovies");
    console.log("mounted");
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-wrap: wrap;
  max-height: calc(100vh - 7em);
  margin-bottom: 2em;
}

main {
  justify-content: center;
  margin-top: 5em;
  display: flex;
  flex:auto;
  flex-direction: row;
  overflow-y: auto;
  max-height: calc(100vh - 10em);
  gap: 3em;
}

a {
  text-decoration: none;
}

.toggle-container {
  display: flex;
  justify-content: flex-end;
  margin-top: 4em;
  margin-bottom: -4em;
  margin-right: 2.4em;
}
.toggle-container p{
  margin: 1em;
  font-size: large;
}

.btn {
  font-size: 17px;
  background: transparent;
  border: none;
  padding: 1em 1.5em;
  color: #ffedd3;
  text-transform: uppercase;
  position: relative;
  transition: 0.5s ease;
  cursor: pointer;
}

.btn::before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 2px;
  width: 0;
  background-color: #e6d054;
  transition: 0.5s ease;
}

.btn:hover {
  color: #1e1e2b;
  transition-delay: 0.5s;
  z-index: 1;
}

.btn:hover::before {
  width: 100%;
}

.btn::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 0;
  width: 100%;
  background-color: #e6d054;
  transition: 0.4s ease;
  z-index: -1;
}

.btn:hover::after {
  height: 100%;
  transition-delay: 0.4s;
  color: aliceblue;
}
.arrow {
  font-size: 2.5em; 
  color: var(--text-light); 
  background: none;
  border: none; 
  padding: 0; 
  transition: border-width 150ms ease-in-out;
  margin-top: -0.5em;
}

.arrow:hover {
  font-size: 2.7em; 
  color:aliceblue;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--secondary-dark);
  z-index: -2;
}

#full {
  height: 100vh;
  background-color: var(--secondary-dark);
  z-index: -2;
}
</style>
