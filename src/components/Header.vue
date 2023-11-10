<template>
    <header class="header">
      <p>Navigation</p>
      <div>
        <router-link to="/">Home</router-link>
        <span class="separator">|</span>
        <router-link to="/signup">Sign up</router-link>
      </div>
    </header>
  </template>
  
  <script>
  export default {
    name: 'Header',
  };
  </script>
  
  <style scoped>
  .header {
  position: fixed;
  background-position-x: center;
  width: 99.6%;
  padding: .5em 0em .5em 0em;
  background-color: #a5a5a5;
  border-radius: 10px;
  display: flex;
  flex-direction: column; 
  align-items: center; 
}

.header p {
  font-size: 1.3em;
  margin-bottom: -0em;
  margin-top: -0em;
}

.header a {
  color: rgb(0, 0, 0);
  text-decoration: none;
  font-size: 1em;
}
.header a:hover {
  color: white;
  text-decoration: none;
  font-size: 1em;
}

.separator {
  font-size: 1.3em;
  margin: 0 10px;
}
  </style>