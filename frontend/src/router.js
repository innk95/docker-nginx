import Vue from 'vue'
import Router from 'vue-router'
import Home from "@/components/Home";
import Profile from "@/components/Profile";

Vue.use(Router)

export default new Router({
  routes: [
      {
          path: '/',
          name: 'home',
          component: Home,
      },
      {
          path: '/profile',
          name: 'profile',
          component: Profile,
          props: true,
      }

  ],


})
