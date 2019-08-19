<template>
  <div class="container">
    <b-table borderless striped hover :items="items" :fields="fields" :tbody-tr-class="'d-flex'" :thead-tr-class="'d-flex'">
    </b-table>
  </div>
</template>

<script>
const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)
const STATUS = ['Todo', 'Solved', 'Tried but in vain']

export default {
  name: 'Probset',
  data () {
    return {
      // fields: ['Id', 'Name', 'Status', 'Submissions AC%', 'Users AC%'],
      fields: [
        { key: 'pid', label: 'Id', thClass: 'col-1', tdClass: 'col-1' },
        { key: 'title', label: 'Name', thClass: 'col-5', tdClass: 'col-5' },
        { key: 'status', label: 'Status', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'submissionsAcRate', label: 'Submissions AC%', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'usersAcRate', label: 'Users AC%', thClass: 'col-2', tdClass: 'col-2' }
      ],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/probs`)
      .then((response) => {
        let data = response.data
        data.forEach(el => {
          el['status'] = STATUS[el['status']]
        })
        this.items = response.data
      })
      .catch((error) => {
        this.items = error
      })
  }
}
</script>

<style lang="css" scoped>
th .m-col-1 {
  max-width: 10px;
}
th .m-col-2 {
  max-width: 20%;
}
th .m-col-5 {
  max-width: 50%;
}
</style>
