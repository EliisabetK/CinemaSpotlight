<template>
  <div class="movie" ref="dynamicContent">
    <img :src="photo" alt="Movie Cover" class="movie-cover">
    <div class="movie-info">
      <router-link :to="'/amovie/' + id">
        <h2>{{ name }} ({{ formatDate(releasedate) }})</h2>
        <p>
          IMDb {{ imdb }} | {{ rottentomatoes > 50 ? '🍅' : '🤢' }} {{ rottentomatoes }}% | Letterboxd {{ letterboxd }}
        </p>
      </router-link>
    </div>
  </div>
</template>
  
  <script>
  export default {
    name: 'Movie2',
    props: ['id', 'photo', 'name', 'imdb', 'letterboxd', 'rottentomatoes', 'releasedate'],
    methods: {
      formatDate(dateString) {
        const releasedate = new Date(dateString);
        const options = { year: 'numeric', month: 'short', day: 'numeric' };
        return releasedate.toLocaleDateString(undefined, options);
      },
    },
    computed: {
    },
  };
  </script>
  
  <style scoped>
  .movie {
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: var(--primary-color);
    margin-bottom: 1em;
    word-wrap: break-word;
    width: 40em;
    height: 7em;
    margin-left: 10em;
    margin-bottom: 4em;
  }
  
  .movie-cover {
    width: 7em;
    height: 7em;
    margin-bottom: -0.1em;
  }
  
  .movie-info {
    text-align: left;
    font-size: 1em;
    color: var(--text-light);
    margin-bottom: 0em;
    margin-left: 2em;
  }
  
  .movie-info h2 {
    font-size: 1.2em;
    color: var(--text-light);
    margin-bottom: -0.1em;
  }
  
  .rating {
    display: inline-block;
    margin-bottom: -1em;
  }
  
  @media (max-width: 600px) {
    .movie-info h3 {
      font-size: 1.2em;
      margin-bottom: 0.25em;
    }
  }
  
  .star {
    color: #e6d054;
    font-size: 30px;
  }
  </style>
  