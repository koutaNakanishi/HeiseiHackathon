const videospeed = 10;//1秒でどれだけ増えるか(開発中に変更すべき)

function addTime() {
    if (videoSetting.isRunning === false)
        return;
    plusTime(videospeed)
}

setInterval(addTime, 1000);//1秒に一回時間を加算する
