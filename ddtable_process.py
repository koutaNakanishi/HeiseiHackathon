def get_ddtable_json(yymm):
    """
    日々の公務のリストをjsonで返す
    形式は
    ```
    {
      {"day": "3","schedule" : "兵庫訪問(明石高専視察)"}
      {"day": "5","schedule" : "三重訪問(伊勢神宮参拝)"}
    }
    ```
    :param yymm: 平成y年m月とすると、(y-1)*12+(m-1)
    :return: 上で示された形式のjson
    """
    return "ddtableのjsonを返す"
