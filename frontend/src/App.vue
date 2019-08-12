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
    Header
  }
}
</script>

<style lang="scss">

@import "./styles/global/_mixin.scss";
@import "./styles/global/markdownstyle.css";

</style>
