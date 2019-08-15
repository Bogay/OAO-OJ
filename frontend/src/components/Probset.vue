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
        { key: 'Id', thClass: 'col-1', tdClass: 'col-1' },
        { key: 'Name', thClass: 'col-5', tdClass: 'col-5' },
        { key: 'Status', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'Submissions AC%', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'Users AC%', thClass: 'col-2', tdClass: 'col-2' }
      ],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/problems`)
      .then((response) => {
        let data = response.data
        data.forEach(el => {
          console.log(el)
          let val = el['Status']
          switch (val) {
            case 1:
              el['Status'] = 'AC'
              break
            case 2:
              el['Status'] = 'WA'
              break
            case 3:
              el['Status'] = 'LLE'
              break
            default:
              el['Status'] = 'Todo'
          }
        })
        this.items = response.data
        console.log('data: ' + this.items)
      })
      .catch((error) => {
        console.log('err: ' + error)
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
