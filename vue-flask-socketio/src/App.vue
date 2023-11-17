<template>
  <div id="app">
    <HelloWorld msg="Welcome to Vue-Flask Socket IO" />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import SocketIO from "socket.io-client";

const socket = SocketIO.connect("http://127.0.0.1:5002");

export default {
  name: "App",
  components: {
    HelloWorld,
  },
  mounted() {
    // this.$refs.text.value = 'text'
    socket.on('connect', () => {
      const data = '连接成功'
      this.$EventBus.$emit('toHello', data)
    });
    socket.on('disconnect', () => {
      const data = '断开连接'
      this.$EventBus.$emit('toHello', data)
    })
    socket.on('message', (data) => {
      this.$EventBus.$emit('toHelloRece', data)
    })
    this.$EventBus.$on('toApp', data => {
      socket.emit("message", data)
    })

  }
};
</script>

<style lang="less">
html,
body,
#app {
  margin: 0;
  padding: 0;
  height: 100%;
}
</style>
