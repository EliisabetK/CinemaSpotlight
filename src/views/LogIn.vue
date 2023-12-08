<!-- võiks teha siia selle et see ütleb vastavalt et vale parool või kasutajat pole kui sisselogimine failib -->
<template>
  <div>
    <div class="container">
      <main>
        <div class="form">
          <h3>Log In</h3>
          <label for="email">Email</label>
          <input type="email" name="email" required v-model="email">
          <label for="password">Password</label>
          <input type="password" name="password" required v-model="password">
          <div class="button-container">
            <button @click="LogIn" class="center">Log in</button>
            <p> Or </p>
            <button @click="$router.push('/signupview')" class="center">Sign up</button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import auth from "../auth";

export default {
  name: "LogIn",
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async LogIn() {
      try {
        const data = {
          email: this.email,
          password: this.password,
        };

        const response = await fetch("http://localhost:3000/auth/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify(data),
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const responseData = await response.json();

        if (responseData.user_id) {
          console.log("Login successful");
          await auth.authenticate();
          this.$router.push("/mainview");
        } else {
          console.log("Login failed:", responseData.error);
        }
      } catch (error) {
        console.error("Fetch error:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  /*min-height: calc(100vh - 4.5em);*/
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
  color: rgb(17, 17, 54);
}

button {
  background: rgb(8, 110, 110);
  border: 0;
  padding: 10px 20px;
  margin: 20px 20px 20px 20px;
  color: white;
  border-radius: 20px;
  align-items: center;
  text-align: center;
}

button:hover {
  background: rgb(27, 154, 154);
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  color: white;
  border-radius: 20px;
  align-items: center;
  text-align: center;
}
.center {
  margin: auto;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  width: 30%;
}

.button-container {
  display: flex;
  justify-content: center;
}
p{
  color: rgb(8, 48, 48);
}
</style>

