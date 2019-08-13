<template>
  <b-card no-body>
    <b-tabs card pills vertical>
      <b-tab v-for="component in componentNames" :title=component :key="component"><component  v-bind:is="component"></component></b-tab>
    </b-tabs>
  </b-card>
</template>

<script>
import Dashboard from './ManageItem/Dashboard'
import Problems from './ManageItem/Problems'
import Contests from './ManageItem/Contests'
import Account from './ManageItem/Account'
import Bulletin from './ManageItem/Bulletin'
import Question from './ManageItem/Question'

export default {
  name: 'Manage',
  components: {
    Dashboard, Problems, Contests, Account, Bulletin, Question
  },
  data () {
    return {
      componentNames: ['Dashboard', 'Problems', 'Contests', 'Account', 'Bulletin', 'Question']
    }
  }
}
</script>

<style lang="css" scoped>
.block {
  background-color: #ddd;
  height: 100%;
  border-radius: 5px;
}
</style>
