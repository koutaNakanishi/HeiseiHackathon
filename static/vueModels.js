
var videoSetting=new Vue({
  el:'#videoSetting',
  data:{
    speed:1000,//1秒あたり加算するスコア(時間)
    spendTime:0,//経過時間の合計
    currentFrame:0,//今のフレーム
    framePerTime:3000,//1フレームあたりのスコア
    isRunning:false
  }

})

//再生ボタン
var startButton = new Vue({
  el: '#startButton',
  data: {
    buttonImage: "/static/images/startButton.png"
  },
  methods: {
    clickStartButton: function () {
      videoSetting.isRunning=!videoSetting.isRunning;
      image_pass = "/static/images/";
      this.buttonImage = image_pass;
      this.buttonImage += (videoSetting.isRunning) ? "pauseButton.png" : "startButton.png";
    }
  }
})

//再生を早くするボタン
var rightButton = new Vue({
  el: '#rightButton',
  data: {
    buttonImage: "/static/images/rightButton.png"
  },
  methods: {
    clickRightButton: function () {
      videoSetting.speed+=200;
    }
  }
})

//再生を遅くするボタン
var rightButton = new Vue({
  el: '#leftButton',
  data: {
    buttonImage: "/static/images/lefttButton.png"
  },
  methods: {
    clickLeftButton: function () {
      videoSetting.speed-=200;
    }
  }
})



var dd_table = new Vue({
  el: '#dd-table',
  data: {
    schedule: "無し"
  }
})

var seken=new Vue({
  el:'#seken',
  data:{
    sekenImage:"/static/images/0.jpg",
    news:"平成の空気の缶詰発売！"
  }
})