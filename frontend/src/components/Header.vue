<template>
  <b-navbar toggleable="lg">
    <b-navbar-brand>OAO Online Judge</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse" ></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-for="item in data" :key="item.name">
          <router-link :to="{ path: item.path }">
            {{ item.name }}
          </router-link>
        </b-nav-item>
      </b-navbar-nav>
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <!-- <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">en-US</b-dropdown-item>
          <b-dropdown-item href="#">ch-TW</b-dropdown-item>
        </b-nav-item-dropdown> -->
        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template slot="button-content">User</template>
          <b-dropdown-item>Profile</b-dropdown-item>
          <b-dropdown-item>Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
var items = [
  { path: '/', name: 'Home' },
  { path: '/problemset', name: 'Problems' },
  { path: '/submissions', name: 'Submissions' },
  { path: '/contests', name: 'Contests' },
  { path: '/discuss', name: 'Discuss' },
  { path: '/about', name: 'About' },
  { path: '/manage/dashboard', name: 'Manage' }
]
export default {
  name: 'Header',
  data () {
    return {
      data: items
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.nav-bar {
  border-bottom-width: 1px;
  border-bottom-style: solid;
}

.navbar-brand {
  color: #2a2f35;
  width: 12%;
  font-size: 1.3vw;
  text-align: center;
}

.nav-link {
  font-size: 1.3vw;
  margin-left: 1vw;
}

</style>
