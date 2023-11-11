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

export default {
  name: 'App',
  components: {
    Footer,
    Header
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
    min-height: calc(100vh - 4.5em);
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
  
  .post-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .profile-image {
    width: 40px;
    height: 40px; 
    object-fit: cover;
    margin-bottom: 1em;
    margin-right: 1em;
  }
  
  main > div > div { /*child selector*/
    background-color: #CBCDBC;
    border-radius: 10px;  
  }
  
  p { /*descendant selector?*/
    color: #293c2e;
    font-size: 1.5em;
    margin-bottom: 0.25em; 
  }
  
  .post{
    padding: 1em;
  }
  
  .post ~ .post { /*general sibling selector*/
    margin-top: 1em;
  }
  
  .like-image{
    margin-bottom: -0.25em;
  }
  
  @media (max-width: 600px) {
    .postImage{
      width:100px;
      height: 100px;
      object-fit:cover;
    }
    .profile-image {
      width: 30px;
      height: 30px;
      object-fit: cover;
    }
    .post p {
      font-size: 0.9em;
    }
    .profile-image + p {
      color: #293c2e; 
      font-size: 1em;
    }
  }
  
  .username {
    color: #293c2e;
    margin-top: -2.7em;
    margin-left: 3.3em; 
    margin-bottom: 2em;
    display: flex;
    align-items: center; 
    font-size: 1.2em;
  }

  .post-header p{
    font-size: 1.1em;
    margin-top: -1.2em;
    color: #454d43;
  }

</style>