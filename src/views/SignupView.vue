<!-- Sign up almost töötab, see authenticateb kasutaja ja tabel on õige aga see ei lähe kohe home viewsse -->
<template>
  <div>
    <div class="container">
      <main>
        <div class="form">
          <h3>SignUp</h3>
          <label for="email">Email</label>
          <input type="email" name="email" required v-model="email">
          <label for="password">Password</label>
          <input type="password" name="password" required v-model="password">
          <button @click="SignUp" class="SignUp">SignUp</button>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data: function () {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    SignUp() {
      var data = {
        email: this.email,
        password: this.password,
      };

      fetch("http://localhost:3000/auth/signup", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);

          if (data.success) {
            console.log("Signup successful");
            this.$router.push("/mainview");
          } else {
            console.log("Signup failed:", data.error);
          }
        })
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  min-height: calc(100vh - 4.5em);
  max-height: calc(100vh - 6.5em);
  column-gap: 3em;
}

main {
  margin-top: 5em;
  flex: 3;
  overflow-y: auto;
  max-height: calc(100vh - 10em);
}

.form {
  max-width: 420px;
  margin: 30px auto;
  background: rgb(186, 202, 210);
  text-align: left;
  padding: 40px;
  border-radius: 10px;
}

h3 {
  text-align: center;
  color: rgb(8, 48, 48);
}

label {
  color: rgb(8, 48, 48);
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

input {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid white;
  color: rgb(13, 13, 52);
}

button {
  background: rgb(8, 110, 110);
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
  align-items: center;
  text-align: center;
}
</style>
