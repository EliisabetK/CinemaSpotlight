<template>
  <div class="info-page">
    <h1>Welcome to CinemaSpotlight</h1>
    <p>
      This website provides an overview list of all the movies currently playing in cinemas in Estonia with ratings from multiple sources.
      Stay in the loop and ensure you never miss the opportunity to catch the next cinematic masterpiece on its release.     </p>

    <h2>References & Resources</h2>
    <ul>
      <li><a href="https://developer.themoviedb.org/docs/getting-started" target="_blank">The website uses TMDb API</a></li>
      <li><a href="https://www.rottentomatoes.com/" target="_blank">Rotten Tomatoes</a></li>
      <li><a href="https://www.letterboxd.com/" target="_blank">Letterboxd</a></li>
      <li><a href="https://www.apollokino.ee/movies" target="_blank">Apollo Kino</a></li>
    </ul>

    <h2>Contact Me</h2>
    <p>
     I value your feedback and suggestions. Please feel free to reach out to me at:
    </p>
    <p>Email: eliisabet.kaasik@gmail.com</p>
  </div>
</template>

<script>
export default {
  name: 'InfoPage',
}
</script>

<style scoped>
.info-page {
  width: 80%;
  margin: auto;
  padding: 20px;
  margin-top: 3em;
}
h2{
  margin-top: 2em;
}
</style>
