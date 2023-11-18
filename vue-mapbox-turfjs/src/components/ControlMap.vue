<template>
    <div class="control-Box">
        <div class="item" v-for="(item, index) in info" :key="index">
            <el-button @click="handle(item)" class="btn">{{ Object.values(item)[0] }}</el-button>
        </div>
    </div>
</template>

<script>
import KrigingData from '../utils/krigingHandle.js'

import { mapState } from 'vuex';

export default {
    data() {
        return {
            info: [
                { pointsShow: '显示点位' },
                { pointHidden: '隐藏点位' },
                { lineShow: '绘制等值线' },
                { lineHidden: '隐藏等值线' },
                { surfaceShow: '绘制等值面' },
                { surfaceHidden: '隐藏等值面' }
            ]
        }
    },
    computed: {
        ...mapState(['map'])
    },
    mounted() {
        this.surfaceInit();
    },
    methods: {
        handle(item) {
            const action = Object.keys(item);
            // 使用方括号动态调用方法
            if (typeof this[action] === 'function') {
                this[action]();
            } else {
                console.error(`Method ${action} not found`);
            }
        },
        pointsShow() {
            this.map.setLayoutProperty('points', 'visibility', 'visible');
        },
        pointHidden() {
            this.map.setLayoutProperty('points', 'visibility', 'none');
        },
        lineShow() {
            this.map.setLayoutProperty('isolines', 'visibility', 'visible');
        },
        lineHidden() {
            this.map.setLayoutProperty('isolines', 'visibility', 'none');
        },
        // 绘制等值面/线
        surfaceInit() {
            const colors = ["#006837", "#1a9850", "#66bd63", "#a6d96a", "#d9ef8b", "#ffffbf",
                "#fee08b", "#fdae61", "#f46d43", "#d73027", "#a50026"]
            const krigingData = new KrigingData();
            const [collection, isolines] = krigingData.generate();
            console.log('collection', collection.features)

            const data = []
            for(let i = 0; i < collection.features.length; i++){
                data.push({
                    lon: collection.features[i].geometry.coordinates[0],
                    lat: collection.features[i].geometry.coordinates[1],
                    value: collection.features[i].properties.value
                })
            }
            // 转换为 GeoJSON 格式
            const geojsonData = {
                type: 'FeatureCollection',
                features: data.map(item => ({
                    type: 'Feature',
                    geometry: {
                        type: 'Point',
                        coordinates: [item.lon, item.lat],
                    },
                    properties: {
                        value: item.value,
                        // 其他属性
                    },
                }))
            }
            console.log(geojsonData)
              console.log(JSON.stringify(geojsonData, null, 2));




            console.log(isolines)
            this.map.on('load', () => {
                this.map.addLayer({
                    id: 'isolines',
                    type: 'line',
                    source: {
                        type: 'geojson',
                        data: isolines,
                    },
                    paint: {
                        'line-color': ['get', 'contour'],
                        'line-opacity': 0.8,
                        'line-width': 1,
                    },
                });
                // 添加等值面图层
                this.map.addLayer({
                    id: 'isobands-layer',
                    type: 'fill',
                    source: {
                        type: 'geojson',
                        data: geojsonData,
                    },
                    paint: {

                        'fill-color': [
                            'match',
                            ['get', 'temperature'],

                            0, colors[0],
                            4, colors[1],
                            8, colors[2],
                            15, colors[3],
                            20, colors[4],
                            25, colors[5],
                            30, colors[6],
                            35, colors[7],
                            40, colors[8],
                            45, colors[9],
                            50, colors[10],
                            /* 默认颜色，可以设置为 fallback 颜色 */
                            colors[0],
                        ], // 根据属性值设置颜色
                        'fill-opacity': 0.8,
                    },
                });
            })
        }
    }
}
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
    }
}
</style>