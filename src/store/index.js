import { createStore } from 'vuex';

export default createStore({
  state: {
    postList: [],
    isAuthenticated: false, // Add isAuthenticated state
  },
  mutations: {
    setPostList(state, posts) {
      state.postList = posts;
    },
    logout(state) {
      state.isAuthenticated = false; // Set isAuthenticated to false when logging out
    },
  },
  actions: {
    async fetchPosts({ commit }) {
      fetch(`http://localhost:3000/api/posts`)
      .then((response) => response.json())
      .then((data) => commit('setPostList', data))
      .catch((e) => console.log(e.message));
    },
    async deletePosts() {
      fetch(`http://localhost:3000/api/posts`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
      })
      .then((response) => response.json())
      .catch((e) => console.log(e));
    },
  },
});
