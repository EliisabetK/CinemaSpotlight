<template>
  <router-link :to="'/amovie/' + id">
    <div class="movie" ref="dynamicContent">
      <img :src="photo" alt="Movie Cover" class="movie-cover">
      <div class="movie-info">
        <h2>{{ name }}</h2>
        <div class="rating">
          <span v-for="star in computedStars" :key="star" class="star">{{ star }}</span>
        </div>
        <p>
            {{ rt_score > 50 ? '🍅' : '🤢' }} {{ rt_score }}%
        </p>
        <p>{{ new Date(releasedate) < currentDate ? 'In cinemas' : formatDate(releasedate) }}</p>
      </div>
    </div>
  </router-link>
</template>

<script>
import formatDate from '@/mixins/formatDate.js';

export default {
  name: 'Movie',
  mixins: [formatDate],
  props: ['id', 'photo', 'name', 'tmdb_score', 'rt_score', 'letterboxd_score', 'releasedate'],
  methods: {
  },
  computed: {
    currentDate() {
      return new Date();
    },    
    computedStars() {
      let stars = '';
      let score = this.letterboxd_score;
      let fullStars = Math.floor(score);
      let halfStar = score - fullStars;
      let emptyStars = 5 - fullStars - 1;
      for (let i = 0; i < fullStars; i++) {
        stars += '\u2605'; // Unicode for a solid star
      }
      if (halfStar >= 0.5) stars += '\u2605';
      else if (halfStar < 0.5) stars += '\u2606';

      for (let i = 0; i < emptyStars; i++) {
        stars += '\u2606'; // Unicode for an empty star
      }
      return stars;
    }

  },
};
</script>

<style scoped>
.movie {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--primary-color);
  margin-bottom: 1em;
  word-wrap: break-word;
  width: 15em;
  transition: background-color 0.4s ease;
  height:26em;
}

.movie:hover {
  background-color: var(--primary-hover); 
}

.movie-cover {
  width: 15em;
  height: 15em;
  margin-bottom: -0.1em;
  object-fit: cover;
}

.movie-info {
  text-align: center;
  font-size: 1em;
  color: var(--text-light);
  margin-bottom: 0em;
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
