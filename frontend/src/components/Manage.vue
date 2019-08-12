<template>
  <div class="container block">
    <b-tabs content-class="mt-3" justified pills>
      <b-tab title="Dashboard" active></b-tab>
      <b-tab title="Problems"></b-tab>
      <b-tab title="Contests"></b-tab>
      <b-tab title="Account"></b-tab>
      <b-tab title="Bulletin"></b-tab>
      <b-tab title="Question"></b-tab>
    </b-tabs>
  </div>
</template>

<script>
export default {
  name: 'Manage',
  data () {
    return {

    }
  }
}
</script>

<style lang="css" scoped>
.block {
  background-color: #ddd;
  height: 40vw;
  border-radius: 15px;
}
</style>
