import Vue from "vue";
import App from "./App.vue";
import store from "./store";


// 事件总线 EventBus
Vue.prototype.$EventBus = new Vue()
// Socket config


Vue.config.productionTip = false;

new Vue({
  store,
  render: (h) => h(App),
}).$mount("#app");
