<template>
  <div>
    <div class="container2">
      <main>
        <div class="contacts">
          <h1 class="contacts-title">Contact us: </h1>
          <div class="contacts-content">
            <div class="contact-item">
              <strong>Email:</strong> Taavi.Taavet@hot.ee
            </div>
            <div class="contact-item">
              <strong>Phone:</strong> +372 5432 1098
            </div>
          </div>
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
.container2 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.container2 main {
  flex: 1;
  text-align: center;
}

.contacts {
  margin-top: 50px;
}

.contacts-title {
  font-size: 2em;
  margin-bottom: 20px;
}

.contacts-content {
  max-width: 600px;
  margin: 0 auto;
}

.contact-item {
  margin-top: 15px;
}

p {
  font-size: 1.2em;
  color: #333;
}
</style>
