# vue-mapbox-turfjs

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

### MapBox
#### 1. 下载 mapbox
```npm install --save mapbox-gl```
#### 2. 在 js 中引入
``` import mapboxgl from 'mapbox-gl'```
#### 3. 地图风格切换
通过使用 vuex 切换 mapbox 的 style属性 实现
### 4. 局部引入 Element-UI
安装 Element ui
```npm install element-ui -S```
main.js 引入
```
import ElementUI from 'element-ui'; // 2.1引入结构
import 'element-ui/lib/theme-chalk/index.css'; // 2.2引入样式
Vue.use(ElementUI); // 3.安装
```

