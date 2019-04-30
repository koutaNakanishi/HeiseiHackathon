import csv
import json
import os


def get_ddtable_json(yymm):
    """
    日々の公務のリストをjsonで返す
    形式は
    ```
    [
        {
            "day": "8",
            "schedule": "経済企画庁事務次官から講義を受ける",
            "place": "赤坂御所"
        },
        {
            "day": "12",
            "schedule": "歌舞演奏会に臨席",
            "place": "楽部"
        },
        {
            "day": "31",
            "schedule": "日本魚類学会年会に出席",
            "place": "国立科学博物館分館"
        }
    ]
    ```
    :param yymm: 平成y年m月とすると、(y-1)*12+(m-1)
    :return: 上で示された形式のjson
    """
    yymm = int(yymm)
    year = yymm // 12 + 1
    month = yymm % 12 + 1
    path = "ddtable/{}/{}/yotei.json".format(year, month)
    if not os.path.exists(path):
        year = (year - 1) % 7 + 1
        path = "ddtable/{}/{}/yotei.json".format(year, month)

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def txt_to_json():
    """
    `/ddtable/[1-30]/[1-12]/yotei.txt`にcsvファイルがあるとして、そこからyotei.jsonを生成する
    csvの例としては
    ```
    8,経済企画庁事務次官から講義を受ける,赤坂御所
    12,歌舞演奏会に臨席,楽部
    31,日本魚類学会年会に出席,国立科学博物館分館
    ```
    jsonの例として
    ```
    [
        {
            "day": "8",
            "schedule": "経済企画庁事務次官から講義を受ける",
            "place": "赤坂御所"
        },
        {
            "day": "12",
            "schedule": "歌舞演奏会に臨席",
            "place": "楽部"
        },
        {
            "day": "31",
            "schedule": "日本魚類学会年会に出席",
            "place": "国立科学博物館分館"
        }
    ]
    ```
    :return: None
    """
    for y in range(1, 32):
        for m in range(1, 13):
            jsondata = []
            csv_path = "ddtable/{}/{}/yotei.txt".format(y, m)

            if not os.path.exists(csv_path):
                continue
            with open(csv_path, "r", encoding="shift-jis") as csvfile:
                reader = csv.DictReader(csvfile, fieldnames=["day", "schedule", "place"])
                for row in reader:
                    jsondata.append(row)

            with open("ddtable/{}/{}/yotei.json".format(y, m), "w", encoding="utf-8") as jsonfile:
                json.dump(jsondata, jsonfile, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    txt_to_json()
