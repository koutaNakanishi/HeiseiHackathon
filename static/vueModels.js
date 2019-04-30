const score_par_month = 100;//変更してはいけない
const SCORE_MIN = 0;
const SCORE_MAX = 30 * 12 * score_par_month;

const videoSetting = new Vue({
    el: '#videoSetting',
    data: {
        time: 0,
        isRunning: false
    }
});

const dd_table = new Vue({
    el: '#dd-table',
    data: {
        schedule: null,
    }
});

const seken = new Vue({
    el: '#seken',
    data: {
        sekenImage: null,
        news: null
    }
});

const show_time = new Vue({
    el: '#show_time',
    computed: {
        yymm: function () {
            return Math.floor(videoSetting.time / score_par_month)
        },
        year: function () {
            return Math.floor(this.yymm / 12) + 1;
        },
        month: function () {
            return this.yymm % 12 + 1;
        }
    },
    watch: {
        yymm: function (val) {
            updateDDTable(val);
            updateSeken(val);
        }
    },
    created: function () {
        updateDDTable(this.yymm)
        updateSeken(this.yymm)
    }
});

function plusTime(time) {//timeは正の数
    videoSetting.time = Math.min(videoSetting.time + time, SCORE_MAX);
}

function minusTime(time) {//timeは正の数
    videoSetting.time = Math.max(videoSetting.time - time, SCORE_MIN);
}

//再生ボタン
const startButton = new Vue({
    el: '#startButton',
    data: {
        buttonImage: "/static/images/startButton.png"
    },
    methods: {
        clickStartButton: function () {
            videoSetting.isRunning = !videoSetting.isRunning;
            const image_pass = "/static/images/";
            this.buttonImage = image_pass;
            this.buttonImage += (videoSetting.isRunning) ? "pauseButton.png" : "startButton.png";
        }
    }
});
//1年早めるボタン
const rightButton = new Vue({
    el: '#rightButton',
    data: {
        buttonImage: "/static/images/rightButton.png"
    },
    methods: {
        clickRightButton: function () {
            plusTime(12 * score_par_month)
        }
    }
});
//1年戻すボタン
const leftButton = new Vue({
    el: '#leftButton',
    data: {
        buttonImage: "/static/images/lefttButton.png"
    },
    methods: {
        clickLeftButton: function () {
            minusTime(12 * score_par_month)
        }
    }
});