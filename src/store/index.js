import { createStore } from 'vuex';

export default createStore({
  state: {
    movieList: [],
  },
  mutations: {
    setMovies(state, movies) {
      state.movieList = movies;
    },
  },
  actions: {
    async fetchMovies({ commit }) {
      fetch(`http://localhost:3000/api/movies`)
      .then((response) => response.json())
      .then((data) => commit('setMovies', data))
      .catch((e) => console.log(e.message));
    },
  },
});
