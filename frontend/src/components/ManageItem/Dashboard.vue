<template>
  <div class="container-fluid">
    <h3>{{ message }}</h3>
    <input type="text" v-model="message">
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data () {
    return {
      message: 'hi'
    }
  }
}
</script>

<style lang="css" scoped>
</style>
