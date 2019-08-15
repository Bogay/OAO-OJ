<template>
  <div class="row">
    <div class="col-2 items">
      <b-nav vertical pills>
        <b-nav-item v-for="comp in comps" :key="comp.name" :to="`/manage/${comp.path}`">
          {{ comp.name }}
        </b-nav-item>
      </b-nav>
    </div>
    <div class="vl"></div>
    <div class="col-9">
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
  padding-left: 4vw;
}

.vl {
  border-left: 2px solid gray;
}
</style>
