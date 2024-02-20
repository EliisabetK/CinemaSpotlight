<template>
    <div class="grid-container">
      <img :src="photo" alt="Movie Cover" class="cover">
      <div class="movie-info info">
        <h2>{{ name }} <span>({{ length }} minutes)</span></h2>
        <h3>{{ director }} ({{ formatDate(releasedate) }})</h3>
        {{ summary }}
      </div>
      <div class="ratings">
        <p>
          TMDb {{ tmdb_score }} | {{ rt_score > 50 ? '🍅' : '🤢' }} {{ rt_score }}% | Letterboxd {{ Math.round(letterboxd_score * 10) / 10 }}
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
        tmdb_score: '',
        rt_score: '',
        letterboxd_score: '',
        releasedate: '',
        length: '',
        summary: '',
        selectedCinema: '',
        cinemas: ['Apollo kino', 'Viimsi kino']
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
            this.tmdb_score = data.tmdb_score;
            this.rt_score = data.rt_score;
            this.letterboxd_score = data.letterboxd_score;
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
    width: 23em;
    height: 23em;
    object-fit: cover;
  }
  
  .info {
    grid-area: info;
    text-align: left;
    background-color: var(--primary-color);
    padding: 2em;
    width: 40em;
    height: 12em;
    overflow-y: auto;
    scrollbar-width: thin;
    scrollbar-color: var(--accent-yellow) var(--primary-color);
  }
  .info p {
    line-height: 150%;
  }
  /* Webkit (Chrome, Safari) scrollbar styles */
  .info::-webkit-scrollbar {
    width: 0.5em;
  }

  .info::-webkit-scrollbar-thumb {
    background-color: var(--accent-yellow);
    border-radius: 6px;
  }

  .info::-webkit-scrollbar-track {
    background-color: var(--primary-color);
  }

  .info h2{
    margin-top: -0em;
  }
  .info h2 span {
    font-weight: lighter;
    font-size: smaller; /* or the desired font weight for the span */
  } 
  h3{
    color: var(--text-color);
  }
  
  .ratings {
    grid-area: ratings;
    padding: 0 2em 0 2em;
    background-color: var(--primary-color);
    justify-content: center;
    display: flex;
    flex-direction: column;
    align-items: center;
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
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  background: url("data:image/svg+xml;utf8,<svg fill='yellow' height='24' viewBox='0 0 24 24' width='24' xmlns='http://www.w3.org/2000/svg'><path d='M7 10l5 5 5-5z'/><path d='M0 0h24v24H0z' fill='none'/></svg>") no-repeat, var(--accent-dark);
  background-position-x: 100%;
  background-position-y: 50%;
}

select option {
  background-color: var(--accent-dark);
}

@media(max-width: 600px) {
    .grid-container {
      grid-template-areas:
        'cover'
        'info'
        'ratings'
        'cinema';
      gap: 10px;
      padding: 10px;
      justify-content: center;
      margin-top: 5em; 
      margin-left: 1em;
      padding-bottom: 5em;
    }

    .cover {
      grid-area: cover;
      width: 90%; 
      height: 15em;
      object-fit: cover;
      margin-top: 0; 
    }

    .info {
      grid-area: info;
      text-align: left;
      background-color: var(--primary-color);
      padding: 1em;
      width: 90%; 
      overflow-y: auto;
      scrollbar-width: thin;
      scrollbar-color: var(--accent-yellow) var(--primary-color);
      margin-top: 1em; 
    }

    .info h2 {
      margin-top: 0;
    }

    .info h2 span {
      font-weight: lighter;
      font-size: smaller;
    }

    h3 {
      color: var(--text-color);
    }

    .ratings {
      grid-area: ratings;
      padding: 1em;
      background-color: var(--primary-color);
      display: flex;
      flex-direction: column;
      align-items: center;
      width:90%; 
    }

    .cinema {
      display: flex;
      grid-area: cinema;
      padding: 1em;
      background-color: var(--primary-color);
      flex-direction: row;
      gap: 1em;
      justify-content: center;
      width: 90%; 
    }
    
    .cover, .info, .ratings, .cinema {
      margin-top: 0.5em;
    }
    #cinema, button {
      width:50%; 
    }
  }
  </style>
  