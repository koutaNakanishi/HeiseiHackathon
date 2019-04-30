import base64
import collections as cl
import json
import os
from os import path


def get_event_json(yymm):
    """
    世の中の情報をjsonで返す
    形式は
    ```
    {
      {"isUpdate": "true"}
      {"image","32a93vaw0b3a..."} //jpg size(*)
      {"caption","この日は長野オリンピックが開催されました"}
    }
    ```
    :param yymm: 平成y年m月とすると、(y-1)*12+(m-1)
    :return: 上で示された形式のjson
    """
    max_yymm_zfill = get_floor_yymm_zfill(yymm)
    data_path = "./seken" + "/" + max_yymm_zfill

    picture_path = data_path + r"/picture.jpg"
    with open(picture_path, 'rb') as f:
        data = f.read()
    image_text = base64.b64encode(data).decode("utf-8")

    caption_path = data_path + r"/caption.txt"
    with open(caption_path, encoding="utf-8") as f:
        caption_text = f.read()

    send_data = cl.OrderedDict()
    send_data["isUpdate"] = "true"
    send_data["image"] = image_text
    send_data["caption"] = caption_text
    send_json = json.dumps(send_data, ensure_ascii=False)
    return send_json


def yymm_to_zfill(yymm):
    year = yymm // 12 + 1
    month = yymm % 12 + 1
    return str(year).zfill(2) + str(month).zfill(2)


def get_floor_yymm_zfill(yymm):
    yymm = int(yymm)
    zfill_yymm = int(yymm_to_zfill(yymm))
    path_list = []
    for directory in os.listdir("./seken"):
        if path.isfile(directory):
            continue
        path_list.append(int(directory))
    floor_pathlist = [x for x in path_list if x <= zfill_yymm]
    max_yymm = max(floor_pathlist)
    return str(max_yymm).zfill(4)


def test_get_floor_yymm_zfill():
    assert get_floor_yymm_zfill(0) == "0101"
    assert get_floor_yymm_zfill(2) == "0101"
    assert get_floor_yymm_zfill(3) == "0104"
    assert get_floor_yymm_zfill(12 * (5 - 1) + 10 - 1) == "0510"
