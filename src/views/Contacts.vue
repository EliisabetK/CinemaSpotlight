<template>
  <div>
    <div class="container">
      <main>
        <div class="contacts">
          <h1 class="contacts-title">Contacts</h1>
          <p>Tere siin on kontaktid</p>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "Contacts",
};
</script>

<style>
.container {
  display: flex;
  /*min-height: calc(100vh - 4.5em);*/
  max-height: calc(100vh - 6.5em);
  column-gap: 3em;
}

.left-column,
.right-column {
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

.contacts {
  margin-top: 100px;
}

.contacts-title {
  margin-top: -100px;
}

p {
  font-size: 20px;
}
</style>
