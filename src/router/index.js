import { createRouter, createWebHashHistory } from 'vue-router';
import MainView from '../views/MainView.vue';
import SignupView from '../views/SignupView.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;