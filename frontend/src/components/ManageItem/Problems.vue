<template>
  <div class="container">
    <b-table head-variant="dark" borderless striped hover :items="items" :fields="fields">
      <template v-for="field in fields" :slot="field.key" slot-scope="data">
        <div v-if="field.colType==='text'" :key="field.key">
          {{ data.item[field.key] }}
        </div>
        <div v-else :key="field.key">
          <router-link :to="`/manage/editpro/${data.item['pid']}`">
            <b-button variant="primary" size="sm">
              Edit
            </b-button>
          </router-link>
        </div>
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
      fields: [
        {key: 'pid', label: 'Id', colType: 'text'},
        {key: 'title', label: 'Name', colType: 'text'},
        {key: 'status', label: 'Status', colType: 'text'},
        {key: 'edit', label: 'Edit', colType: 'button'}
      ],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/admin/probs`)
      .then((response) => {
        let data = response.data
        data.forEach(el => {
          let val = el['status']
          switch (val) {
            case 1:
              el['status'] = 'Offline'
              break
            case 2:
              el['status'] = 'Hidden'
              break
            default:
              el['status'] = 'Online'
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

</style>
