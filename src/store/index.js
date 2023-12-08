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
      try {
        const response = await fetch('http://localhost:3000/posts');
        const data = await response.json();
        commit('setPostList', data);
      } catch (error) {
        console.error('Error fetching posts:', error);
      }
    },
  },
});
