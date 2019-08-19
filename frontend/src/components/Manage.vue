<template>
  <div class="row container-fluid">
    <div class="col-2 items">
      <b-nav vertical pills>
        <b-nav-item v-for="comp in comps" :key="comp.name" :to="`/manage/${comp.path}`" class="item">
          {{ comp.name }}
        </b-nav-item>
      </b-nav>
    </div>
    <div class="col-10">
      <router-view/>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Manage',
  data () {
    return {
      comps: [
        { path: 'dashboard', name: 'Dashboard' },
        { path: 'problems', name: 'Problems' },
        { path: 'contests', name: 'Contests' },
        { path: 'account', name: 'Account' },
        { path: 'bulletin', name: 'Bulletin' },
        { path: 'question', name: 'Question' }
      ]
    }
  }
}
</script>

<style lang="css" scoped>

.items {
  height: 80vh;
  padding-left: 2vw;
  border-right: 0.2vw solid #50514f;
}

.item {
  border-bottom: 0.1vw solid #50514f;
}
</style>
