///////動画再生のために、必要な処理を書いていく
const videospeed = 10;//1秒でどれだけ増えるか(開発中に変更すべき)

function changeDDTable() {

    const url = URL + "/dd-table";
    const request = new XMLHttpRequest();
    request.open('GET', url);

    request.onreadystatechange = function () {
        if (request.readyState !== 4) {
            //リクエスト中
            console.log("リクエスト中");
        } else if (request.status !== 200) {
            //失敗
            console.log("リクエスト失敗");
        } else {
            dd_table.schedule = request.responseText;
        }
    };
    request.send();

}

function changeNews() {
    const url = URL + "/event";
    const request = new XMLHttpRequest();
    request.open('GET', url);

    request.onreadystatechange = function () {
        if (request.readyState !== 4) {
            //リクエスト中
            console.log("リクエスト中");
        } else if (request.status !== 200) {
            //失敗
            console.log("リクエスト失敗");
        } else {
            event.news = request.responseText;
        }
    };
    request.send();
}


function addTime() {
    if (videoSetting.isRunning === false)
        return;
    plusTime(videospeed)
}

function intToYYMM(time) {
    yymm = Math.floor(time / score_par_month)
    year = Math.floor(yymm / 12);
    month = yymm % 12;
}

function changeFrame() {
    changeDDTable();
    // changeNews();
}

setInterval(addTime, 1000);//1秒に一回時間を加算する
