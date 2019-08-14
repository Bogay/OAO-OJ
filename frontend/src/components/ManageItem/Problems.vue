<template>
  <div>
    <b-collapse id="prob-detail">
      <b-card>
        <h2>ha, 想編輯題目? 自己來做啦哈哈哈哈哈哈哈哈嗚嗚嗚嗚嗚</h2>
      </b-card>
    </b-collapse>
    <div class="container">
      <b-table head-variant="dark" borderless striped hover :items="items" :fields="fields">
        <template v-for="field in fields" :slot="field.key" slot-scope="data">
          <div v-if="field.colType==='text'" :key="field.key">
            {{ data.item[field.key] }}
          </div>
          <div v-else :key="field.key">
            <b-button variant="primary" size="sm" v-b-toggle.prob-detail>
              Edit
            </b-button>
          </div>
        </template>
      </b-table>
    </div>
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
        {key: 'Id', label: 'Id', colType: 'text'},
        {key: 'Name', label: 'Name', colType: 'text'},
        {key: 'Status', label: 'Status', colType: 'text'},
        {key: 'Edit', label: 'Edit', colType: 'button'}
      ],
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
