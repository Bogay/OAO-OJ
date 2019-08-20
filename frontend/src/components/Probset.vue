<template>
  <div class="container">
    <b-table borderless striped hover :items="items" :fields="fields" :tbody-tr-class="'d-flex'" :thead-tr-class="'d-flex'">
      <span slot="title" slot-scope="data">
        <router-link :to="`/pro/${data.item.pid}`">{{ data.item.title }}</router-link>
      </span>
      <span slot="status" slot-scope="data" v-bind:style="{ color: STATUS_COLOR[data.item.status] }">
        {{ STATUS[data.item.status] }}
      </span>
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
        { key: 'pid', label: 'Id', thClass: 'col-1', tdClass: 'col-1' },
        { key: 'title', label: 'Name', thClass: 'col-5', tdClass: 'col-5' },
        { key: 'status', label: 'Status', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'submissionsAcRate', label: 'Submissions AC%', thClass: 'col-2', tdClass: 'col-2' },
        { key: 'usersAcRate', label: 'Users AC%', thClass: 'col-2', tdClass: 'col-2' }
      ],
      items: [],
      STATUS: ['Todo', 'Solved', 'Tried but in vain'],
      STATUS_COLOR: ['#000', '#3ae061', '#ff5475']
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/probs`)
      .then((response) => {
        this.items = response.data
      })
      .catch((error) => {
        console.log(error)
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
