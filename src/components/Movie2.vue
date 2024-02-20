<template>
  <div class="movie" ref="dynamicContent">
    <img :src="photo" alt="Movie Cover" class="movie-cover">
    <div class="movie-info">
      <router-link :to="'/amovie/' + id">
        <h2>{{ name }} ({{ formatDate(releasedate) }})</h2>
        <p>
          TMDb {{ tmdb_score }} | {{ rt_score > 50 ? '🍅' : '🤢' }} {{ rt_score }}% | Letterboxd {{ Math.round(letterboxd_score * 10) / 10 }}
        </p>
      </router-link>
    </div>
  </div>
</template>
  
  <script>
  import formatDate from '@/mixins/formatDate.js';
  export default {
    name: 'Movie2',
    mixins: [formatDate],
    props: ['id', 'photo', 'name', 'tmdb_score', 'rt_score','letterboxd_score', 'releasedate'],
    methods: {
    
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
    transition: background-color 0.4s ease;

  }
  .movie:hover {
  background-color: var(--primary-hover); 
}
  .movie-cover {
    width: 7em;
    height: 7em;
    margin-bottom: -0.1em;
    object-fit: cover;

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
  @media(max-width: 600px){
    .movie{
      width: 27em;
    }
  }


  </style>
  