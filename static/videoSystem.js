///////動画再生のために、必要な処理を書いていく

function changeDDTable() {

    url = URL + "/dd-table";
    var request = new XMLHttpRequest();
    request.open('GET', url);

    request.onreadystatechange = function () {
        if (request.readyState != 4) {
            //リクエスト中
            console.log("リクエスト中");
        } else if (request.status != 200) {
            //失敗
            console.log("リクエスト失敗");
        } else {
            dd_table.schedule = request.responseText;

        }
    };
    request.send();
}

function changeNews() {
    url = URL + "/event";
    var request = new XMLHttpRequest();
    request.open('GET', url);

    request.onreadystatechange = function () {
        if (request.readyState != 4) {
            //リクエスト中
            console.log("リクエスト中");
        } else if (request.status != 200) {
            //失敗
            console.log("リクエスト失敗");
        } else {
            event.news=request.responseText;
        }
    };
    request.send();
}


function addTime() {
    if (videoSetting.isRunning == false)
        return;
    videoSetting.spendTime += videoSetting.speed;
    nextFrame = Math.floor(videoSetting.spendTime / videoSetting.framePerTime);

    if (nextFrame > videoSetting.currentFrame) {//動画を次のフレームに更新
        changeFrame();
        videoSetting.currentFrame = nextFrame;
    }
}

function intToYYMM(frame){
    year=Math.floor(frame/12);
    month=frame%12;
}

function changeFrame() {
    changeDDTable();
    // changeNews();
}
setInterval("addTime()", 1000);//1秒に一回時間を加算する
