import { createStore } from 'vuex';

export default createStore({
  state: {
    postList: [],
  },
  mutations: {
    setPostList(state, posts) {
      state.postList = posts;
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
