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
      </router-link>    
    </div>
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
    async fetchPosts() {
      const fetchPostsQuery = `SELECT * FROM "posts";`;

      try {
        const response = await fetch("http://localhost:3000/fetchposts", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          credentials: "include",
          body: JSON.stringify({ query: fetchPostsQuery }),
        });

        const data = await response.json();
        this.$store.commit("updatePostList", data.rows);
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    },
    async logout() {
      try {
        await fetch("http://localhost:3000/auth/logout", {
          credentials: "include",
        });
        this.$store.commit('logout');
        this.$router.push("/login");
      } catch (error) {
        console.error("Error during logout:", error);
      }
    },
    async deleteAllPosts() {

    },
  },
  mounted() {
    this.$store.dispatch('fetchPosts');
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
  background: rgb(8, 110, 110);
  color: rgb(233, 235, 235);
  text-decoration: none;
  font-size: medium;
}
button:hover {
  border: 0;
  margin: 0.25em;
  padding: 10px 20px;
  border-radius: 20px;
  align-items: center;
  text-align: center;
  display: flex;
  justify-content: center;
  background: rgb(27, 154, 154);
  color: rgb(241, 241, 241);
  text-decoration: none;
  font-size: medium;
}

.container {
  display: flex;
  max-height: calc(100vh - 7em);
  column-gap: 3em;
}

.left-column, .right-column {
    flex: 1;
    background-color: #7597ad;
    border-radius: 10px;
    margin-top: 5em;
    position: sticky;
    z-index: 1;
    min-height: calc(100vh - 9.5em);
    max-height: calc(100vh - 9.5em);
  }

main {
  margin-top: 5em;
  flex: 3;
  overflow-y: auto;
  max-height: calc(100vh - 10em);
}
a{
  text-decoration: none;
}

</style>
