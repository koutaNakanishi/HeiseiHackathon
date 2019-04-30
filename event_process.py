import base64
import collections as cl
import json
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
    yymm = int(yymm)
    yy = yymm // 12 + 1
    mm = yymm % 12 + 1
    yy = str(yy)
    yy = yy.zfill(2)
    mm = str(mm)
    mm = mm.zfill(2)
    yymm_string = yy + mm
    data_path = r"./seken/" + yymm_string

    if not path.exists(data_path):
        send_data = cl.OrderedDict()
        send_data["isUpdate"] = "false"
        send_data["image"] = None
        send_data["caption"] = None
        send_json = json.dumps(send_data, ensure_ascii=False)
        return send_json  # jsonにアップデートなしで出力
    else:
        target_file = data_path + r"/picture.jpg"
        with open(target_file, 'rb') as f:
            data = f.read()
        image_text = base64.b64encode(data).decode("utf-8")

        target_file = data_path + r"/caption.txt"
        with open(target_file, encoding="utf-8") as f:
            caption_text = f.read()

        send_data = cl.OrderedDict()
        send_data["isUpdate"] = "true"
        send_data["image"] = image_text
        send_data["caption"] = caption_text
        send_json = json.dumps(send_data, ensure_ascii=False)
        return send_json
