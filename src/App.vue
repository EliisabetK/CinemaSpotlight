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
  background-color: #eae3d9
}

  /* Home page CSS elements */

  .like-image{
    height: 35px;
    width: 35px;
  }
  
  .postImage{
    width:250px;
    height: 250px;
    object-fit:cover;
  }
  
  .container {
    display: flex;
    /*min-height: calc(100vh - 4.5em);*/
    max-height: calc(100vh - 6.5em);
    column-gap: 3em;
  }
  
  .left-column, .right-column {
    flex: 1;
    background-color: #7597ad;
    border-radius: 10px;
    margin-top: 5em;
    position: sticky;
    z-index: -1;
  }
  
  main {
    margin-top: 5em;
    flex: 3; 
    overflow-y: auto; 
    max-height: calc(100vh - 10em); 
  }
  

</style>