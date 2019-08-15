<template>
  <div class="container">
    <div class="row">
      <b-img thumbnail src="/static/temp.jpg" alt="Responsive image"></b-img>
      <div class="col">
        <h3>{{ message }}</h3>
        <b-form-input type="text" v-model="message"></b-form-input>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Contests',
  data () {
    return {
      message: 'say something'
    }
  }
}
</script>

<style lang="css" scoped>

</style>
