<template>
  <div class="hello">
    <textarea v-model="textArea" readonly="readonly" wrap="hard"></textarea>
    <input v-model="textInput" @keyup.enter="send" type="text" class="text">
    <button @click="send">发送</button>
  </div>
</template>

<script>


export default {
  name: "HelloWorld",
  data() {
    return {
      textArea: '聊天室\n',
      textInput: ''
    }
  },
  props: {
    msg: String,
  },
  mounted() {
    // 连接、断开
    this.$EventBus.$on('toHello', data => {
      this.showStatus(data)
    })
    // 接收服务端信息
    this.$EventBus.$on('toHelloRece', data => {
      this.showStatus(data, 'rece')
    })
  },
  methods: {
    send() {
      // let text = this.$refs.input.value;
      // this.$refs.input.value =  ''
      if (this.textInput == '') return;
      // 发送到屏幕上
      this.showStatus(this.textInput, 'send')
      // 发送给服务端
      this.$EventBus.$emit('toApp', this.textInput)
      this.textInput = '';
    },
    // 发送到屏幕上
    showStatus(text, type = null) {
      if (type == 'send') {
        this.textArea = this.textArea + '\n' + '客户端： ' + text;
      } else if (type == 'rece') {
        this.textArea = this.textArea + '\n' + '服务端： ' + text;
      } else {
        this.textArea = this.textArea + '\n' + '-----------' + text + '-----------';
      }
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="less">
.hello {
  position: absolute;
  width: 100%;
  height: 100%;

  textarea {
    border: 0;
    outline: 0;
    padding: 0;
    margin: 0;
    width: 100%;
    height: calc(100% - 70px);
    resize: none;
    caret-color: transparent; //不显示光标
    background-color: antiquewhite;
    font: 400 18px "华文细黑", sans-serif;
  }

  input {
    border: 0;
    outline: 0;
    border: 5px solid skyblue;
    caret-color: skyblue; // 光标颜色
    width: calc(90% - 10px);
    padding: 0;
    height: 50px;
    font: 400 18px "华文细黑", sans-serif;
    color: rgb(17, 17, 19);
  }

  button {
    width: 10%;
    height: 60px;
    margin: 0;
    padding: 0;
    border: 0;
    color: aliceblue;
    font: 400 18px "华文细黑", sans-serif;
    background-color: chocolate;
  }
}
</style>
