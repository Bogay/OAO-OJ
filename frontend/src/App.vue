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

<style>
@import url('https://fonts.googleapis.com/css?family=Noto+Sans+TC&display=swap');
@import url('https://fonts.googleapis.com/css?family=Noto+Serif+TC&display=swap');
@import url('https://fonts.googleapis.com/css?family=IBM+Plex+Serif&display=swap');

@font-face {
    font-family: custom;
    src: local('Noto Serif TC'), local('Noto Sans TC');
    unicode-range: U+00-024F;
}

@font-face {
    font-family: custom;
    src: local('Noto Serif TC'), local('Noto Sans TC');
    unicode-range: U+4E00-9FFF;
}

body {
  font-family: 'IBM Plex Serif', custom;
  background-color: #f5f2f0;
}

::-webkit-scrollbar {
  width: 0.5vw;
}

::-webkit-scrollbar-track {
  -webkit-border-radius: 10px;
  border-radius: 10px;
}

::-webkit-scrollbar-thumb {
  -webkit-border-radius: 4px;
  border-radius: 4px;
  background: rgb(219,219,219);
}

</style>
