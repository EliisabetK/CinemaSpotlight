<template>
    <header class="header">
      <p>Navigation</p>
      <div>
        <router-link to="/mainview">Home</router-link>
        <span class="separator">|</span>
        <router-link to="/contacts">Contacts</router-link>
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
  background-color: #7597ad;
  border-radius: 10px;
  display: flex;
  flex-direction: column; 
  align-items: center; 
}

.header p {
  font-size: 1.5em;
  margin-bottom: -0em;
  margin-top: -0em;
  color: #ECECEA;
}

.header a {
  color: #ECECEA;
  text-decoration: none;
  font-size: 1.2em;
}
.header a:hover {
  color: #E4C49E;
  text-decoration: none;
  font-size: 1.2em;
}

.separator {
  font-size: 1.3em;
  margin: 0 10px;
  color: #ECECEA;
}
  </style>