import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import AMovie from "../views/AMovie.vue";
import Info from "../views/Info.vue";

const routes = [

  {
    path: "/home",
    name: "Home",
    component: Home,
  },

  {
    path: "/AMovie/:movieId",
    name: "AMovie",
    component: AMovie,
  },
  {
    path: "/info",
    name: "Info",
    component: Info,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
