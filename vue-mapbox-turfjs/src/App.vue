<template>
  <div id="app">
    <MapBox />
  </div>
</template>

<script>
import MapBox from './components/MapBox.vue'

export default {
  name: "App",
  components: {
    MapBox,
  },
};
</script>

<style lang="less">
body {
  margin: 0;
  padding: 0;
}

#app {
  // height: 100vh;
  margin: 0;
  padding: 0;
}
</style>
