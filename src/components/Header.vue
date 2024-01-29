<template>
  <header class="header">
    <div>
      <router-link to="/Home" @click.native="scrollToTop">HOME</router-link>
      <span class="separator">|</span>
      <router-link to="/Info">INFO</router-link>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      });
    },
  },
};
</script>

<style scoped>
.header {
  position: fixed;
  width: 100%;
  padding: 0.7em;
  background: linear-gradient(to bottom, rgba(100, 101, 102, 0.5), transparent);
  display: flex;
  flex-direction: column;
  align-items: left;
  position: fixed;
  top: 0;
  z-index: 1000;
  margin-left: -1em;
  padding-left: 3em;
}

.header p {
  font-size: 1.5em;
  margin-bottom: -0em;
  margin-top: -0em;
  color: var(--text-light);
}

.header a {
  color: var(--text-light);
  text-decoration: none;
  font-size: 1.2em;
  padding: 1em;
}
.header a:hover {
  color: #e6d054;
  text-decoration: none;
  font-size: 1.2em;
}

.separator {
  font-size: 1.3em;
  margin: 0 10px;
  color: var(--text-light);
}
</style>
