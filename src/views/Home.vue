<template>
  <div>
    <div class="toggle-container">
      <button class="btn" @click="toggleInCinemas(true)">In cinemas</button>
      <button class="btn" @click="toggleInCinemas(false)">Coming soon</button>
    </div>
    <div class="container">
      <main>
        <Movie
          v-for="movie in topRatedMovies"
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
    <div class="arrowscroll">
      <button @click="scrollToFull" class="arrow">﹀</button>
    </div>
    <div id="full" class="full-section">
      <video id="fullVideo" playsinline autoplay muted loop>
        <source src="@/assets/background.mp4" type="video/mp4">
      </video>
      <div class="empty"></div>
      <div class="allMovies">
        <select id="order" v-model="orderBy" class="select-css">
        <option value="rating" class="option">Rating</option>
        <option value="alphabet" class="option">Alphabet</option>
    </select>
        <Movie2
          v-for="movie in orderedMovies"
          :key="movie.id"
          :id="movie.id"
          :photo="movie.photo"
          :name="movie.name"
          :imdb="movie.imdb"
          :letterboxd="movie.letterboxd"
          :rottentomatoes="movie.rottentomatoes"
          :releasedate="movie.releasedate"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Movie from "@/components/Movie.vue";
import Movie2 from "@/components/Movie2.vue";
import { scrollTo } from "vue-scrollto";

export default {
  name: "Home",
  data() {
    return {
      inCinemas: true,
      orderBy: 'rating', // Default order by rating
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
    topRatedMovies() {
      return this.filteredMovies.sort((a, b) => b.letterboxd - a.letterboxd).slice(0, 4);
    },

    orderedMovies() {
      switch (this.orderBy) {
        case 'alphabet':
          return this.filteredMovies.slice().sort((a, b) => a.name.localeCompare(b.name));
        case 'length':
          return this.filteredMovies.slice().sort((a, b) => a.length - b.length);
        default: // rating
          return this.filteredMovies.slice().sort((a, b) => b.letterboxd - a.letterboxd);
      }
    },
  },
  components: {
    Movie, Movie2
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
  color: var(--text-dark);
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
  background-color: var(--accent-yellow);
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
  margin-top: -1em;
}

.arrow:hover {
  font-size: 2.7em; 
  color:aliceblue;
}

.container {
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: -2;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}

#full {
  min-height: 150%;
  height: 100vh;
  z-index: 0;
  position: relative;
}
#full video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: -1;
}
.arrowscroll {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 3em;
}

#order {
    margin-top: 4em;
    margin-left: 65em;
    padding: 0.5em 1em;
    font-size: 1em;
    border: 3px solid var(--primary-dark);
    border-radius: 5px;
    background-color: var(--primary-color);
    color: #e6d054;
    width: 10%;
    appearance: none;
    background-image: url('data:image/svg+xml;charset=US-ASCII,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%22292.4%22%20height%3D%22292.4%22%3E%3Cpath%20fill%3D%22%23e6d054%22%20d%3D%22M287%2069a18%2018%200%200%200-13-5H18c-5%200-9%203-12%207a18%2018%200%200%200-1%2013c0%205%202%2010%205%2013l128%20128c4%204%2010%205%2013%205s9-1%2013-5L287%2082c4-3%205-8%205-13%200-5-1-9-5-13z%22%2F%3E%3C%2Fsvg%3E');
    background-repeat: no-repeat;
    background-position: right .7em top 50%;
    background-size: .65em auto;
}

#order:focus {
    outline: none;
}

.option {
  border-color: var(--primary-hover);
  border-radius: 5px;
  padding: 5px;
  transition: 300ms;
  background-color: #2a2f3b;
  width: 150px;
  font-size: 15px;
}

.option:hover {
  background-color: #323741;
  border-color: var(--primary-hover);
  font-size: 25px;
  outline: none;
}

.select-css:focus {
    outline: none;
}

.select-css .option {
    border: 1px solid var(--primary-dark);
    outline: none !important;
    background-color: var(--background-color);
    color: var(--text-color);
}

.select-css .option:hover {
    background-color: #323741 !important; 
    color: #e6d054 !important; 
}

.empty {
  height: 4.5em;
}
</style>
