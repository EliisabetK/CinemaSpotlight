<template>
    <div class="grid-container">
      <img :src="photo" alt="Movie Cover" class="cover">
      <div class="movie-info info">
        <h2>{{ name }} ({{ formatDate(releasedate) }})</h2>
        <p>
          IMDb {{ imdb }} | {{ rottentomatoes > 50 ? '🍅' : '🤢' }} {{ rottentomatoes }}% | Letterboxd {{ letterboxd }}
        </p>
        {{ summary }}
      </div>
      <div class="length">
        <p>Length: <input v-model="length" type="number" min="0"> mins</p>
      </div>
      <div class="cinema-selection cinema">
        <label for="cinema">Select a cinema:</label>
        <select id="cinema" v-model="selectedCinema">
          <option disabled value="">Please select one</option>
          <option v-for="cinema in cinemas" :value="cinema">{{ cinema }}</option>
        </select>
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
        photo: '',
        name: '',
        imdb: '',
        letterboxd: '',
        rottentomatoes: '',
        releasedate: '',
        length: '',
        summary: '',
        selectedCinema: '',
        cinemas: ['Cinema 1', 'Cinema 2', 'Cinema 3'] // Add your cinemas here
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
      'cover cover length length cinema cinema';
    gap: 10px;
    padding: 10px;
    justify-content: center;
    margin-top: 7em;
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
  
  .length {
    grid-area: length;
    padding: 2em;
    background-color: var(--primary-color);

  }
  
  .cinema {
    grid-area: cinema;
    padding: 2em;
    background-color: var(--primary-color);
  }
  </style>
  