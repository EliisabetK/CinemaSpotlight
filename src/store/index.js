import { createStore } from 'vuex';

export default createStore({
  state: {
    postList: [
      {id: 0, date: "2023-10-01T08:00:00", text: "See on esimene postitus. Sisaldab ainult teksti.", creator_name: "Jaan Tamm", likeCount: 0},
      {id: 1, date: "2023-10-01T10:30:00", text: "Teine postitus pildiga.", image_url: "https://i.ibb.co/tCRjqMV/sad-ant-with-bindle.jpg", creator_name: "Liis Mägi", likeCount: 0},
      {id: 2, date: "2023-10-01T12:45:00", text: "Tekstipostitus.", creator_name: "Mati Mets", likeCount: 0},
      {id: 3, date: "2023-10-01T15:15:00", text: "Postitus teise pildiga.", image_url :"https://i.ibb.co/CvyDgvY/hamer.jpg", creator_name: "Eva Lepik", likeCount: 0},
      {id: 4, date: "2023-10-02T09:20:00", text: "Viies postitus nimekirjas.", creator_name: "Peeter Vähi", likeCount: 0},
      {id: 5, date: "2023-10-21T11:00:00", text: "Postitus palju sisuga. aaaaaaaaaaaaaaaa aaaaaaa  aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.", creator_name:"Siiri Saar", likeCount: 0},
      {id: 6, date: "2023-10-02T13:40:00", text: "Jällegi tekstipostitus.", creator_name: "Mart Kask", likeCount: 0},
      {id: 7, date: "2023-10-02T16:10:00", text: "Pildiga postitus detailidega.", image_url: "https://i.ibb.co/fHvRSR8/mina.jpg", creator_name: "Olavi Luik", likeCount: 0},
      {id: 8, date: "2023-10-03T10:50:00", text: "Üheksas postitus sel lehel.", creator_name: "Kristi Teder", likeCount: 0},
      {id: 9, date: "2023-10-03T12:30:00", text: "Viimane postitus nimekirjas.", creator_name:"Toomas Lepp", likeCount: 0}
    ]
  },
  getters: {
  },
  mutations: {
    incrementLikeCount(state, postIndex) {
      state.postList[postIndex].likeCount++;
    }, 
    resetLikeCount: state => {
      state.postList.forEach(post => {
        post.likeCount = 0;
      })
    },
  },
  actions: {
  },
  modules: {
  }
});
