import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Probset from '@/components/Probset'
import Submissions from '@/components/Submissions'
import Contests from '@/components/Contests'
import Discuss from '@/components/Discuss'
import About from '@/components/About'
import Manage from '@/components/Manage'
import ManageDash from '@/components/ManageItem/Dashboard'
import ManageProb from '@/components/ManageItem/Problems'
import ManageCont from '@/components/ManageItem/Contests'
import ManageAcco from '@/components/ManageItem/Account'
import ManageBull from '@/components/ManageItem/Bulletin'
import ManageQues from '@/components/ManageItem/Question'
import EditPro from '@/components/ManageItem/Editpro'
import Pro from '@/components/Pro'

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
      component: Manage,
      children: [
        { path: 'dashboard', component: ManageDash },
        { path: 'problems', component: ManageProb },
        { path: 'contests', component: ManageCont },
        { path: 'account', component: ManageAcco },
        { path: 'bulletin', component: ManageBull },
        { path: 'question', component: ManageQues },
        { path: 'editpro/:pid', component: EditPro }
      ]
    },
    {
      path: '/pro/:id',
      name: 'Pro',
      component: Pro
    }
  ]
})
