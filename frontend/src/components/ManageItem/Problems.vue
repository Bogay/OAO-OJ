<template>
  <div class="container">
    <b-row align-h="start">
      <b-col cols="2">
        <router-link to="/manage/editpro/new" style="white-space: nowrap;">
          <b-button variant="primary" style="font-size: 1em">
            new problem
          </b-button>
        </router-link>
      </b-col>
    </b-row>
    <b-table head-variant="dark" borderless striped hover :items="items" :fields="fields" :tbody-tr-class="'d-flex'" :thead-tr-class="'d-flex'">
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
const STATUS = ['Online', 'Offline', 'Hidden']

export default {
  name: 'Problems',
  data () {
    return {
      fields: [
        {key: 'pid', label: 'Id', colType: 'text', thClass: 'col-1', tdClass: 'col-1'},
        {key: 'title', label: 'Name', colType: 'text', thClass: 'col-7', tdClass: 'col-7'},
        {key: 'status', label: 'Status', colType: 'text', thClass: 'col-2', tdClass: 'col-2'},
        {key: 'edit', label: '', colType: 'button', thClass: 'col-2', tdClass: 'col-2'}
      ],
      items: []
    }
  },
  mounted () {
    this.$http.get(`${API_BASE_URL}/admin/probs`)
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

</style>
