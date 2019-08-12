import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Probset from '@/components/Probset'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/problemset',
      name: 'Probset',
      component: Probset
    },
    {
      path: '/submissions',
      name: 'Submissions'
    },
    {
      path: '/contests',
      name: 'Contests'
    },
    {
      path: '/discuss',
      name: 'Discuss'
    },
    {
      path: '/about',
      name: 'About'
    },
    {
      path: '/manage',
      name: 'Manage'
    }
  ]
})
