<template>
  <div class="container">
    <table>
      <thead>
        <tr>
          <td>#</td>
          <td>name</td>
          <td>status</td>
          <td>ac</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="i in 10">
          <td v-for="j in 4">
            {{j}}
          </td>
        </tr>
      </tbody>
    </table>
    <!-- <b-table striped hover :items="items">
    </b-table> -->
  </div>
</template>

<script>
// const API_PORT = ':8000'
// const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)
// var data = this.$http.get(API_BASE_URL)
// console.log(data)
export default {
  name: 'Probset',
  data () {
    return {
      // items: data
    }
  }
}
</script>

<style lang="css" scoped>
</style>
