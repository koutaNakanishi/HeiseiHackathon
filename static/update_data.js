function updateDDTable(yymm) {
    let url = URL + "/dd-table" + "?yymm=";
    url += String(yymm);
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
            dd_table.schedule = JSON.parse(request.responseText);
        }
    };

    request.send();
}

function updateSeken(yymm) {
    let url = URL + "/event" + "?yymm=";
    url += String(yymm);
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
            const someObj = JSON.parse(request.responseText);
            console.log(someObj);
            if (someObj.isUpdate === "true") {
                const prefix = "data:image/jpg;base64,";
                seken.sekenImage = prefix + someObj.image;
                seken.news = someObj.caption;
            }
        }
    };

    request.send();
}