<template>
    <div class="baseMap">
        <div v-for="(image, index) in images" :key="index" class="image-item">
            <img class="img" :class="{ 'selected': selectedIndex === index}"
             :src="image.src" @click="handleButtonClick(index)" :alt="'Image ' + (index + 1)">
            <div class="text">{{ text[index] }}</div>
        </div>
    </div>
</template>

<script>
import { mapMutations } from 'vuex';

export default {
    data() {
        return {
            images: [
                { src: 'baseMap/day.png' },
                { src: 'baseMap/night.png' },
                { src: 'baseMap/satellite.png' }
            ],
            text: ['地图', '夜间', '影像'],
            text_layers: ['day', 'night', 'satellite'],
            selectedIndex: 0,
        }
    },
    methods: {
        ...mapMutations(['baseSwitch']),
        handleButtonClick(index) {
            // 改变state中 current 的值
            this.baseSwitch(this.text_layers[index])
            this.selectedIndex = index; // 追踪当前选中图片的索引
        },
    }
}
</script>

<style>
.baseMap {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 300px;
    height: 120px;
    background-color: rgb(184, 184, 187);
    display: flex;
    justify-content: space-between;
    .image-item {
        /* position: absolute; */
        width: 100px;
        text-align: center;
        margin-bottom: 20px;
        padding-top: 5px;
        .img {
            width: 80px;
            height: auto;
            border: 4px solid rgba(233, 235, 238, 0.664);
        }
        .img:hover {
            /* 鼠标悬停时的样式 */
            cursor: pointer;
        }
        .selected {
            border: 4px solid rgba(8, 189, 221, 0.664);
        }
        .text {
            font: 400 16px '华文黑体';
        }
    }
}
</style>