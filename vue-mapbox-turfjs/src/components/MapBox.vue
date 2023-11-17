<template>
    <div id="mapbox" class="map">
    </div>
</template>
  
<script>
import mapboxgl from 'mapbox-gl'
export default {
    data() {
        return {
            key: 'pk.eyJ1IjoibGw5NTI3IiwiYSI6ImNscDJmdGY2ZTBxMXkyam84OTExODRkZW8ifQ.SaHvgg2sUG1Zq4tQslFW5w'
        }
    },
    mounted(){
        this.init()
    },
    methods: {
        init() {
            mapboxgl.accessToken = this.key;
            var map = new mapboxgl.Map({
                container: 'mapbox', // container id 绑定的组件的id
                style: 'mapbox://styles/mapbox/streets-v11', //地图样式，可以使用官网预定义的样式,也可以自定义
                center: [120.2, 30.1666], // 初始地图中心点位置
                zoom: 15,     // starting zoom 地图初始的层级
                pitch: 60,  //地图的角度，不写默认是0，取值是0-60度，一般在3D中使用
                bearing: -17.6, //地图的初始方向，值是北的逆时针度数，默认是0，即是正北
                antialias: true, //抗锯齿，通过false关闭提升性能
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
</style>
  