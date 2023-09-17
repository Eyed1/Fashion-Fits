import { createRouter, createWebHistory } from 'vue-router'
import FitsView from '../views/FitsView.vue'
import WardropeView from '../views/WardropeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'fits',
      component: FitsView 
    },
    {
      path: '/wardrope',
      name: 'wardrope',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: WardropeView
    }
  ]
})

export default router
