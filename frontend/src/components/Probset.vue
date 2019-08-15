<template>
  <div class="container">
    <b-table borderless striped hover :items="items" :fields="fields" :tbody-tr-class="'d-flex'" :thead-tr-class="'d-flex'">
    </b-table>
  </div>
</template>

<script>
const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)

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
          let val = el['status']
          switch (val) {
            case 1:
              el['status'] = 'Solved'
              break
            case 2:
              el['status'] = 'Tried but in vain'
              break
            default:
              el['status'] = 'Todo'
          }
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
