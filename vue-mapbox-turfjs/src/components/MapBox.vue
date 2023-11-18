<template>
    <div id="mapbox" class="map">
    </div>
</template>
  
<script>
import mapboxgl from 'mapbox-gl'
import { mapState } from 'vuex';
import { mapMutations } from 'vuex';

export default {
    data() {
        return {
            jsonData: null,
            key: 'pk.eyJ1IjoibGw5NTI3IiwiYSI6ImNscDJmdGY2ZTBxMXkyam84OTExODRkZW8ifQ.SaHvgg2sUG1Zq4tQslFW5w'
        }
    },
    computed: {
        // vuex state 数据
        ...mapState(['baseMap', 'map']),
        baseMapStyle() {
            return this.baseMap.current;
        }
    },
    mounted() {
        // 使用 require 引入 JSON 文件
        this.jsonData = require('@/assets/temperature.json');
        this.init() // 初始化页面

    },
    watch: {
        // 监听 this.$store.state.baseMap.current 的值
        baseMapStyle(newVal, odlVal) {
            this.map.once('styledata', () => {
                this.addPoints();
            });

            this.map.setStyle(newVal);

        }
    },
    methods: {
        ...mapMutations(['mapInit']),
        // 初始化页面
        init() {
            mapboxgl.accessToken = this.key;
            var map = new mapboxgl.Map({
                container: 'mapbox', // container id 绑定的组件的id
                // style: this.baseMap.current, //地图样式，可以使用官网预定义的样式,也可以自定义
                center: [121.56, 29.86], // 初始地图中心点位置
                zoom: 9,     // starting zoom 地图初始的层级
                pitch: 0,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
                bearing: 0, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
                antialias: true, //抗锯齿，通过false关闭提升性能
                optimizeForTerrain: true, //启用地形
                trackResize: true, //随浏览器窗口缩放调整
                attributionControl: false,  //隐藏底部Mapbox Logo 或者在css中也可以实现
            });
            map.setStyle(this.baseMap.current)
            map.on('load', () => {
                this.addPoints();
            })
            this.mapInit(map)
        },
        // 添加点数据
        addPoints() {
            this.map.addSource('points', {
                type: 'geojson',
                data: this.jsonData
            });
            // 设置点的样式
            this.map.addLayer({
                id: 'points',
                type: 'circle',
                source: 'points',
                paint: {
                    'circle-radius': 6,
                    'circle-color': '#FF0000' // 替换为你想要的点的颜色
                }
            });
        }
    }
};
</script>
  
<style lang="less">
.map {
    width: 100%;
    height: 100%;
    position: absolute;
}

// 将 canvas 全屏显示
#mapbox>div.mapboxgl-canvas-container.mapboxgl-interactive.mapboxgl-touch-drag-pan.mapboxgl-touch-zoom-rotate>canvas {
    width: 100%;
    height: 100%;
    position: absolute;
}
</style>
  