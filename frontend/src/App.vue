<template>
  <div id="app">
    <Header></Header>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header'
export default {
  name: 'App',
  components: {
    'Header': Header
  }
}
</script>

<style lang="scss">

@import "./styles/global/_mixin.scss";
@import "./styles/global/markdownstyle.css";

</style>
