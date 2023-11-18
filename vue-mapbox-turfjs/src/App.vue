<template>
  <div id="app">
    <MapBox />
    <BaseMap />
    <ControlMap />
  </div>
</template>

<script>
import MapBox from './components/MapBox.vue'
import BaseMap from './components/BaseMap.vue'
import ControlMap from './components/ControlMap.vue'
import LST from './utils/simulatedData.js'


export default {
  name: "App",
  mounted() {
    // 生成模拟数据
    // const lst = new LST();
    // const geojsonData = lst.generateRandomTemperatureData(300, { min: 120, max: 122 }, { min: 28, max: 30 }, { min: 10, max: 30 });
    // console.log(JSON.stringify(geojsonData, null, 2));
  },
  components: {
    MapBox,
    BaseMap,
    ControlMap
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
