<template>
  <div class="container">
    <h1>{{ $route.params.pid }}</h1>
    <h2>{{ items.title }}</h2>
    <div class="container">
      <vue-markdown>{{ items.desc }}</vue-markdown>
    </div>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'
const API_PORT = ':8000'
const API_BASE_URL = location.origin.replace(/:\d+/g, API_PORT)

export default {
  name: 'Editpro',
  data () {
    return {
      items: []
    }
  },
  components: {
    VueMarkdown
  },
  mounted () {
    console.log(`${API_BASE_URL}/probs/${this.$route.params.pid}`)
    this.$http.get(`${API_BASE_URL}/probs/${this.$route.params.pid}`)
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
