<template>
  <div>
    <div class="container">
      <aside class="left-column"></aside>
      <main>
        <div>
          <Post
            v-for="post in postList"
            :key="post.id"
            :id="post.id"
            :post_date="post.date"
            :post_text="post.text"
          />
        </div>
      </main>
      <aside class="right-column"></aside>
    </div>
    <div class="button-container">
      <button @click="logout">Logout</button>
      <button @click="deleteAllPosts">Delete All</button>
      <router-link to="/addpost">
        <button class="add-post-button">Add Post</button>
      </router-link>    </div>
  </div>
</template>

<script>
import Post from "@/components/Post.vue";

export default {
  name: "MainView",
  data() {
    return {
      postText: "",
    };
  },
  computed: {
    postList() {
      return this.$store.state.postList;
    },
  },
  components: {
    Post,
  },
  methods: {
    logout() {
      fetch("http://localhost:3000/auth/logout", {
        credentials: "include",
      })
        .then((response) => response.json())
        .then(() => {
          this.$store.commit("logout");
          this.$router.push("/login");
        })
        .catch((error) => {
          console.log("Error during logout:", error);
        });
    },
    deleteAllPosts() {
      // Add logic to delete all posts
      console.log("Deleting all posts");
    },
  },
};
</script>

<style scoped>
.button-container {
  display: flex;
  justify-content: center;
}

button {
  border: 0;
  margin: 0.25em;
  padding: 10px 20px;
  border-radius: 20px;
  align-items: center;
  text-align: center;
  display: flex;
  justify-content: center;
  background-color: rgb(160, 197, 235);
  color: rgb(24, 31, 31);
  text-decoration: none;
  font-size: medium;
}

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

</style>
