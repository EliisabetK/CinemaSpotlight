<template>
  <div>
    <div class="container">
      <main>
        <div class="form">
          <h3>Add Post</h3>
          <label for="postText">Post Text</label>
          <textarea name="postText" required v-model="postText"></textarea>
          <div class="button-container">
            <button @click="addPost" class="center">Add Post</button>
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddPost",

  data: function () {
    return {
      postText: "",
    };
  },
  methods: {
    addPost() {
      var data = {
        text: this.postText,
      };

      fetch("http://localhost:3000/addpost", {
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
          // Redirect or perform other actions after adding the post
        })
        .catch((e) => {
          console.log(e);
          console.log("error");
        });
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
  color: rgb(8, 48, 48)
}

label {
  color: rgb(8, 49, 49);
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

textarea {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid white;
  color: rgb(25, 25, 93);
  resize: vertical;
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
</style>
