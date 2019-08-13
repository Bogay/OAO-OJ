<template>
  <div class="container block">
    <b-tabs content-class="mt-3" justified pills vertical>
      <b-tab title="Dashboard" active>
        <DashBoard></DashBoard>
      </b-tab>
      <b-tab title="Problems"></b-tab>
      <b-tab title="Contests"></b-tab>
      <b-tab title="Account"></b-tab>
      <b-tab title="Bulletin"></b-tab>
      <b-tab title="Question"></b-tab>
    </b-tabs>
  </div>
</template>

<script>
import Dashboard from './ManageItem/Dashboard'
export default {
  name: 'Manage',
  component: {
    'Dashboard': Dashboard
  },
  data () {
    return {
      message: 'h3'
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
