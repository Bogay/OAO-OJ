<template>
  <div class="container">
    <div class="row">
      <b-img thumbnail src="https://pbs.twimg.com/media/D5Xwu2BVUAEDBUx?format=jpg&name=small" alt="Responsive image"></b-img>
      <div class="col">
        <h3>{{ message }}</h3>
        <b-form-input type="text" v-model="message"></b-form-input>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Problems',
  data () {
    return {
      message: 'say something'
    }
  }
}
</script>

<style lang="css" scoped>

</style>
