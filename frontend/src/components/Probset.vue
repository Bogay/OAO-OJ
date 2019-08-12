<template>
  <div class="container">
    <b-table striped hover :items="items" :fields="fields">
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
      fields: [
        { key: 'Id', tdClass: 'col-1' },
        { key: 'Name', tdClass: 'col-5' },
        { key: 'Status', tdClass: 'col-2' },
        { key: 'Submissions AC%', tdClass: 'col-2' },
        { key: 'Users AC%', tdClass: 'col-2' }
      ],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/problems`)
      .then((response) => {
        let data = response.data
        data.forEach(el => {
          let val = el[2]
          switch (val) {
            case 1:
              el[2] = 'AC'
              break
            case 2:
              el[2] = 'WA'
              break
            case 3:
              el[2] = 'LLE'
              break
            default:
              el[2] = 'none'
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
</style>
