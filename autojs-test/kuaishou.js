home();
// console.show();
const appName = "快手";
launchApp(appName);

sleep(1000);
let a = 6;

// const text1 = text('7.5万').findOnce();
// console.log(text1.bounds())
// console.log(text1.bounds().left)
// console.log(text1.bounds().top)

while (a) {
  // 获取屏幕的宽度和高度
  var screenWidth = device.width;
  var screenHeight = device.height;
  // 定义滑动的起始点和结束点
  var startX = screenWidth / 2; // 屏幕中心点的X坐标
  var startY = screenHeight * 0.8; // 屏幕底部
  var endX = screenWidth / 2; // 屏幕中心点的X坐标
  var endY = screenHeight * 0.2; // 屏幕顶部

  // 定义滑动持续时间（单位：毫秒）
  var duration = 3; // 1秒

  //点赞
  click(946, 1129)

  sleep(1000)

  //取消点赞
  click(946, 1129)

  sleep(2000)
  // 执行滑动操作
  swipe(startX, startY, endX, endY, duration);
  sleep(1000);
  a--
}
