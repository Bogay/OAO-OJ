<template>
  <b-container>
    <b-row>
      <b-col class="col-8">
        <vue-markdown>{{ introMD }}</vue-markdown>
      </b-col>
      <b-col class="col-4">
        <vue-markdown>{{ devlogMD }}</vue-markdown>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import intro from '../assets/intro.md'
import devlog from '../assets/devlog.md'
import VueMarkdown from 'vue-markdown'
export default {
  name: 'Home',
  data () {
    return {
      introMD: intro,
      devlogMD: devlog
    }
  },
  components: {
    VueMarkdown
  }
}
</script>

<style scoped>
</style>
