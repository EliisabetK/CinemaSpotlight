<template>
  <div id="app">
    <Header> </Header>
    <router-view />
    <Footer></Footer>
  </div>
</template>

<script>
import Footer from '@/components/Footer.vue';
import Header from '@/components/Header.vue';
import Post from '@/components/Post.vue';

export default {
  name: 'App',
  components: {
    Footer,
    Header,
    Post
  },
};
</script>

// General style of the app
<style>

body {
  font-family: monospace, sans-serif;
  margin: 0;
  padding: 0.2em;
  background-color: #eae3d9;
}

</style>