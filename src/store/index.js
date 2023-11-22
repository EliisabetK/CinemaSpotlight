import { createStore } from 'vuex'

export default createStore({
  state: {
        postList:[
          {date:"2023-10-01T10:30:00",text:"Teine postitus pildiga.",image_url:"https://i.ibb.co/tCRjqMV/sad-ant-with-bindle.jpg",creator_name:"Liis Mägi"},
          {date:"2023-10-01T15:15:00",text:"Postitus teise pildiga.",image_url:"https://i.ibb.co/CvyDgvY/hamer.jpg",creator_name:"Eva Lepik"},
        ]
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})