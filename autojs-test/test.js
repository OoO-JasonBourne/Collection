// home();
// // console.show();
// const appName = "学习强国";
// launchApp(appName);

// sleep(2000);

// const score = text("积分").findOnce();

// // 找到分数所在的位置并点击
// if (score) {
//   const posi = score.bounds();
//   click(posi.left + 100, posi.top);
//   sleep(1000);
// }
// const completedButton = text("去看看").findOnce();
// if (completedButton) {
//   completedButton.click();
//   sleep(2000);
//   let yaowen = text("要闻").findOnce();
//   // let yaowenPosi = yaowen.bounds();
//   // click(yaowenPosi.left, yaowenPosi.top)
//   // log(yaowenPosi)

//   // 我要选读文章
//   if (yaowen) {
//     let bobao = text("播报").findOnce();
//     bobao.click()
//     console.log("bobao1", bobao);

//     sleep(2000);
//     // 获取屏幕的宽度和高度
//     var screenWidth = device.width;
//     var screenHeight = device.height;

//     // 定义滑动的起始点和结束点
//     var startX = screenWidth / 2; // 屏幕中心点的X坐标
//     var startY = screenHeight * 0.8; // 屏幕底部
//     var endX = screenWidth / 2; // 屏幕中心点的X坐标
//     var endY = screenHeight * 0.2; // 屏幕顶部

//     // 定义滑动持续时间（单位：毫秒）
//     var duration = 3; // 1秒

//     // 执行滑动操作
//     swipe(startX, startY, endX, endY, duration);

//     bobao = text("播报").findOnce();
//     bobao.click()
//     console.log("bobao2", bobao);
//   }
// }
