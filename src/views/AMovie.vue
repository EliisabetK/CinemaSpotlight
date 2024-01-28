<template>
    <div class="grid-container">
      <img :src="photo" alt="Movie Cover" class="cover">
      <div class="movie-info info">
        <h2>{{ name }} ( {{ length }} min )</h2>
        <h3>{{ director }} ({{ formatDate(releasedate) }})</h3>
        {{ summary }}
      </div>
      <div class="ratings">
        <p>
          IMDb {{ imdb }} | {{ rottentomatoes > 50 ? '🍅' : '🤢' }} {{ rottentomatoes }}% | Letterboxd {{ letterboxd }}
        </p>
      </div>
      <div class="cinema-selection cinema">
        <select id="cinema" v-model="selectedCinema">
          <option disabled value="">Select a cinema</option>
          <option v-for="cinema in cinemas" :value="cinema">{{ cinema }}</option>
        </select>
        <button @click="directToSite(value)">Buy tickets</button>
      </div>
    </div>
  </template>
  
  <script>
  import formatDate from '@/mixins/formatDate.js';

  export default {
    name: 'AMovie',
    mixins: [formatDate],
    data() {
      return {
        id: '',
        director: '',
        photo: '',
        name: '',
        imdb: '',
        letterboxd: '',
        rottentomatoes: '',
        releasedate: '',
        length: '',
        summary: '',
        selectedCinema: '',
        cinemas: ['Apollo kino', 'Viimsi kino'] // Add your cinemas here
      }
    },
    methods: {
      fetchMovie() {
        const id = this.$route.params.id;
        console.log(id);
        fetch(`http://localhost:3000/api/movies/${id}`)
          .then((response) => response.json())
          .then((data) => {
            console.log(data);
            this.id = data.id;
            this.director = data.director;
            this.photo = data.photo;
            this.name = data.name;
            this.imdb = data.imdb;
            this.letterboxd = data.letterboxd;
            this.rottentomatoes = data.rottentomatoes;
            this.releasedate = data.releasedate;
            this.length = data.length;
            this.summary = data.summary;          
          })
          .catch((error) => {
            console.error('Error fetching movie:', error);
          });
      },
      directToSite() {
        if(this.selectedCinema == 'Viimsi kino'){
          window.location.href = window.open("https://www.viimsikino.ee/Movies/NowInTheatre", '_blank');
        }
        else if(this.selectedCinema == 'Apollo kino'){
          window.location.href = window.open("https://www.apollokino.ee/movies", '_blank');
        }
      }
    },
    mounted() {
      this.fetchMovie();
    }
  };
  </script>
  
  <style scoped>
  .grid-container {
    display: grid;
    grid-template-areas:
      'cover cover info info info info'
      'cover cover info info info info'
      'cover cover ratings ratings cinema cinema';
    gap: 10px;
    padding: 10px;
    justify-content: center;
    margin-top: 10em;
  }
  
  .cover {
    grid-area: cover;
    width: 20em;
    height: 20em;
  }
  
  .info {
    grid-area: info;
    text-align: left;
    background-color: var(--primary-color);
    padding: 2em;
  }
  .info h2{
    margin-top: -0em;
  }
  
  .ratings {
    grid-area: ratings;
    padding: 0 2em 0 2em;
    background-color: var(--primary-color);
    justify-content: center;
    display: flex;
    flex-direction: column;
  }
  
  .cinema {
    display: flex;
    grid-area: cinema;
    padding: 0.5em 2em 0.5em 2em;
    background-color: var(--primary-color);
    flex-direction: column;
    gap: 1em;
    justify-content: center;
  }
  .info h3 {
    font-weight: lighter;
  }
  select, button {
    padding: 0.5em;
    font-size: 1em;
    border-radius: 5px;
    border: none;
    background-color: var(--accent-dark); 
  }

  select:hover, select:focus, select::selection, select:active {
    border: none;
    outline: none !important;

  }

  button {
    background-color: var(--accent-yellow); 
    color: var(--text-dark); 
    cursor: pointer;
  }

  button:hover {
    background-color: var(--accent-yellow-hover);
  }
  select {
    -moz-appearance:none; 
    -webkit-appearance:none; 
    appearance:none;
}
  </style>
  