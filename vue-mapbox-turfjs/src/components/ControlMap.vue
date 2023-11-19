<template>
  <div class="control-Box">
    <div class="item" v-for="(item, index) in info" :key="index">
      <el-button
        @click="handle(item)"
        class="btn"
        :class="{ btn: !item.active, 'btn-active': item.active }"
        >{{ Object.values(item)[0] }}</el-button
      >
    </div>
  </div>
</template>

<script>
import KrigingData from "../utils/krigingHandle.js";

import { mapState, mapMutations } from "vuex";

const colors = [
  "#006837",
  "#1a9850",
  "#66bd63",
  "#a6d96a",
  "#d9ef8b",
  "#ffffbf",
  "#fee08b",
  "#fdae61",
  "#f46d43",
  "#d73027",
  "#a50026",
];

const color_style = [
  "match",
  ["get", "value"],
  -30,
  colors[0],
  -22,
  colors[1],
  -14,
  colors[2],
  -6,
  colors[3],
  2,
  colors[4],
  10,
  colors[5],
  18,
  colors[6],
  26,
  colors[7],
  34,
  colors[8],
  42,
  colors[9],
  50,
  colors[10],
  /* 默认颜色，可以设置为 fallback 颜色 */
  "#FFF",
];
const krigingData = new KrigingData();
const [isolines, isobands] = krigingData.generate();

export default {
  data() {
    return {
      info: [
        { pointShow: "显示点位", active: true },
        { pointHidden: "隐藏点位", active: false },
        { lineShow: "绘制等值线", active: false },
        { lineHidden: "隐藏等值线", active: true },
        { surfaceShow: "绘制等值面", active: false },
        { surfaceHidden: "隐藏等值面", active: true },
        { labelShow: "显示标注", active: false },
        { labelHidden: "隐藏标注", active: true },
      ],
    };
  },
  computed: {
    ...mapState(["map", "layerStatus", "baseMap"]),
    pointStatus() {
      return this.layerStatus.point;
    },
    lineStatus() {
      return this.layerStatus.line;
    },
    surfaceStatus() {
      return this.layerStatus.surface;
    },
    labelStatus() {
      return this.layerStatus.label;
    },
  },
  mounted() {
    this.surfaceInit();
    this.$EventBus.$on("surfaceInit", (data) => {
      this.map.on("styledata", () => {
        this.addLine(); //添加线
        this.addLabel(); // 添加 SymbolLayer 用于显示数值标签
        this.addSurface(); // 绘制等值面
        // 设置图层显隐
        this.map.setLayoutProperty(
          "points",
          "visibility",
          this.pointStatus ? "visible" : "none"
        );
        this.map.setLayoutProperty(
          "isolines",
          "visibility",
          this.lineStatus ? "visible" : "none"
        );
        this.map.setLayoutProperty(
          "isobands",
          "visibility",
          this.surfaceStatus ? "visible" : "none"
        );
        this.map.setLayoutProperty(
          "isolines-labels",
          "visibility",
          this.labelStatus ? "visible" : "none"
        );
      });
    });
  },
  watch: {
    pointStatus(newVal, oldVal) {
      // if(newVal){
      //   this.map.setLayoutProperty("points", "visibility", "visible");
      // }else{
      //   this.map.setLayoutProperty("points", "visibility", "none");
      // }
      // 设置图层显隐
      this.map.setLayoutProperty(
        "points",
        "visibility",
        newVal ? "visible" : "none"
      );
      // 改变 active 值切换按钮样式
      this.info[0].active = newVal;
      this.info[1].active = !newVal;
    },
    lineStatus(newVal, oldVal) {
      this.map.setLayoutProperty(
        "isolines",
        "visibility",
        newVal ? "visible" : "none"
      );
      // 改变 active 值切换按钮样式
      this.info[2].active = newVal;
      this.info[3].active = !newVal;
    },
    surfaceStatus(newVal, oldVal) {
      this.map.setLayoutProperty(
        "isobands",
        "visibility",
        newVal ? "visible" : "none"
      );
      // 改变 active 值切换按钮样式
      this.info[4].active = newVal;
      this.info[5].active = !newVal;
    },
    labelStatus(newVal, oldVal) {
      this.map.setLayoutProperty(
        "isolines-labels",
        "visibility",
        newVal ? "visible" : "none"
      );
      // 改变 active 值切换按钮样式
      this.info[6].active = newVal;
      this.info[7].active = !newVal;
    },
  },
  methods: {
    ...mapMutations(["changeLayerStatus"]),
    handle(item) {
      const action = Object.keys(item)[0];
      // 使用方括号动态调用方法
      if (typeof this[action] === "function") {
        this[action]();
      } else {
        console.error(`Method ${action} not found`);
      }
    },
    pointShow() {
      this.changeLayerStatus({ atti: "point", status: true });
    },
    pointHidden() {
      this.changeLayerStatus({ atti: "point", status: false });
    },
    lineShow() {
      this.changeLayerStatus({ atti: "line", status: true });
    },
    lineHidden() {
      this.changeLayerStatus({ atti: "line", status: false });
    },
    surfaceShow() {
      this.changeLayerStatus({ atti: "surface", status: true });
    },
    surfaceHidden() {
      this.changeLayerStatus({ atti: "surface", status: false });
    },
    labelShow() {
      this.changeLayerStatus({ atti: "label", status: true });
    },
    labelHidden() {
      this.changeLayerStatus({ atti: "label", status: false });
    },
    // 绘制等值线
    addLine() {
      // 使用 some 方法判断是否存在 该图层
      const allLayers = this.map.getStyle().layers; // 图层
      const ifhas = allLayers.some((item) => item.id == "isolines");
      if (ifhas) return;
      this.map.addLayer({
        id: "isolines",
        type: "line",
        source: {
          type: "geojson",
          data: isolines,
        },
        paint: {
          // 假设你的属性叫做'value'，包含范围信息
          "line-color": color_style,
          "line-opacity": 1,
          "line-width": 2,
        },
      });
    },
    // 绘制等值面
    addSurface() {
      // 使用 some 方法判断是否存在 该图层
      const allLayers = this.map.getStyle().layers; // 图层
      const ifhas = allLayers.some((item) => item.id == "isobands");
      if (ifhas) return;
      this.map.addLayer({
        id: "isobands",
        type: "fill",
        source: {
          type: "geojson",
          data: isolines,
        },
        paint: {
          "fill-color": color_style,
          "fill-opacity": 0.8,
        },
      });
    },
    // 添加标签
    addLabel() {
      // 使用 some 方法判断是否存在 该图层
      const allLayers = this.map.getStyle().layers; // 图层
      const ifhas = allLayers.some((item) => item.id == "isolines-labels");
      if (ifhas) return;
      this.map.addLayer({
        id: "isolines-labels",
        type: "symbol",
        source: {
          type: "geojson",
          data: isolines,
        },
        layout: {
          "text-field": ["to-string", ["get", "value"]],
          "text-size": 18,
          "text-anchor": "center",
        },
        paint: {
          "text-color": "#ff0000",
        },
      });
    },
    // 绘制等值面/线
    surfaceInit() {
      //   const data = [];
      //   for (let i = 0; i < collection.features.length; i++) {
      //     data.push({
      //       lon: collection.features[i].geometry.coordinates[0],
      //       lat: collection.features[i].geometry.coordinates[1],
      //       value: collection.features[i].properties.value,
      //     });
      //   }
      this.map.on("styledata", () => {
        this.addLine(); //添加线
        this.addLabel(); // 添加 SymbolLayer 用于显示数值标签
        this.addSurface(); // 绘制等值面

        this.map.setLayoutProperty(
          "isolines",
          "visibility",
          this.lineStatus ? "visible" : "none"
        ),
          this.map.setLayoutProperty(
            "isobands",
            "visibility",
            this.surfaceStatus ? "visible" : "none"
          ),
          this.map.setLayoutProperty(
            "isolines-labels",
            "visibility",
            this.labelStatus ? "visible" : "none"
          );
      });
    },
  },
};
</script>

<style lang="less" scoped>
.control-Box {
  position: absolute;
  top: 180px;
  right: 20px;

  .item {
    .btn {
      width: 112px;
    }
    .btn-active {
      background-color: rgb(83, 188, 230);
      color: #fff;
    }
  }
}
</style>
