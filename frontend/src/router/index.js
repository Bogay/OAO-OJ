import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Probset from '@/components/Probset'
import Submissions from '@/components/Submissions'
import Contests from '@/components/Contests'
import Discuss from '@/components/Discuss'
import About from '@/components/About'
import Manage from '@/components/Manage'

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
      name: 'Submissions',
      component: Submissions
    },
    {
      path: '/contests',
      name: 'Contests',
      component: Contests
    },
    {
      path: '/discuss',
      name: 'Discuss',
      component: Discuss
    },
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/manage',
      name: 'Manage',
      component: Manage
    }
  ]
})
