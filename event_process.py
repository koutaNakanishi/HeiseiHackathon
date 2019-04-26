def get_event_json(yymm):
    """
    世の中の情報をjsonで返す
    形式は
    ```
    {
      {"isUpdate": "true"}
      {"image","32a93vaw0b3a..."}
      {"caption","この日は長野オリンピックが開催されました"}
    }
    ```
    :param yymm: 平成y年m月とすると、(y-1)*12+(m-1)
    :return: 上で示された形式のjson
    """
    return "世の中の情報のjsonを返す"
