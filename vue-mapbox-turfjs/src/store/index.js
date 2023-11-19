import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    map: null,
    layerStatus: {
      point: true,
      line: false,
      surface: false,
      label: false,
    },
    baseMap : {
      current: 'mapbox://styles/mapbox/streets-v11',
      day: 'mapbox://styles/mapbox/streets-v11',
      night: 'mapbox://styles/mapbox/navigation-guidance-night-v2',
      satellite: 'mapbox://styles/mapbox/satellite-v9'
    }
  },
  getters: {},
  mutations: {
    baseSwitch(state, style){
      // 通过传入的字符串使用动态属性名的方式来实现切换current实现不同的地图样式
      if (state.baseMap.hasOwnProperty(style)) {
        state.baseMap.current = state.baseMap[style];
      }
    },
    mapInit(state, map){
      // 为 map 赋值
      state.map = map
    },
    changeLayerStatus(state, payload) {
      const { atti, status } = payload;
      // 动态属性绑定
      state.layerStatus[atti] = status;
    }   
  },
  actions: {},
  modules: {},
});
