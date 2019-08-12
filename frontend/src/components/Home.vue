<template>
  <vue-markdown>
    {{ data }}
  </vue-markdown>
</template>

<script>
import intro from '../assets/intro.md'
import VueMarkdown from 'vue-markdown'
export default {
  name: 'Home',
  data () {
    return {
      data: intro
    }
  },
  components: {
    VueMarkdown
  }
}
</script>

<style scoped>
</style>
