<template>
  <div class="container">
    <b-table head-variant="dark" borderless striped hover :items="items" :fields="fields">
      <template>
        <b-button variant="primary" size="sm">
          Edit
        </b-button>
      </template>
    </b-table>
  </div>
</template>

<script>
const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)

export default {
  name: 'Problems',
  data () {
    return {
      fields: ['Id', 'Name', 'Status', 'Edit'],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/admin/problems`)
      .then((response) => {
        this.items = response.data
        console.log('data: ' + this.items)
      })
      .catch((error) => {
        this.items = error
        console.log('err: ' + error)
      })
  }
}
</script>

<style lang="css" scoped>

</style>
