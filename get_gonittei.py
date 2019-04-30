import locale
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def get_detail_gonittei_url_from_top_page():
    """
    メインページ(http://www.kunaicho.go.jp/page/gonittei/top/1)から30(31)年間の4半期ごとのデータがあるページへのリンクを辿る
    :return: None
    """
    base_url = "http://www.kunaicho.go.jp/"
    url = urljoin(base_url, "page/gonittei/top/1")
    response = requests.get(url)
    bs_obj = BeautifulSoup(response.content, "html.parser")

    table = bs_obj.find("table", {"class": "normal w90per"})
    rows = table.findAll("tr")
    for row in rows:
        row.find("th").text  # example "平成元年"
        links = row.findAll("li")
        for item in links:
            url = item.find("a").get("href")
            url = urljoin(base_url, url)
            url  # example "http://www.kunaicho.go.jp/activity/gonittei/01/h01/gonitei-h01-01.html"
            item.text  # example "1月～3月"
            get_detail(url)


def get_detail(url):
    """
    ご日程の詳細ページから、その日の日付や予定のリストを解析する
    :param url: 詳細ページのurl
    e.g. "http://www.kunaicho.go.jp/activity/gonittei/01/h01/gonitei-h01-01.html"
    :return: None
    """
    response = requests.get(url)
    bs_obj = BeautifulSoup(response.content, "html.parser")
    section = bs_obj.find("div", {"class": "section"})
    date = section.find("h2").text
    date  # example "平成元年（1月～3月）"
    tables = section.find("ul", {"class": "program"}).findAll("li")
    for table in tables:
        get_each_day_detail(table)


def get_each_day_detail(table_for_one_day):
    day = table_for_one_day.find("caption").text
    prefix, day = parse_date_string(day)
    rows = table_for_one_day.findAll("tr")[1:]  # リストの1つめはデータではないのでいらない
    koumu = []
    for row in rows:
        tds = row.findAll("td")
        if len(tds) > 1:
            koumu += tds[1]
        elif len(tds) == 1:
            koumu += tds[0]

    # print(prefix+str(day)+"日")
    # print(koumu)


def parse_date_string(date):
    """
    日付文字列を解析する
    :param date:
    :return: 平成何年の何月かの文字列, 月の中の日 のtuple
    """
    # date = GY年M月D日（DOW）
    date = date.replace(" ", "").replace("　", "").replace("\n", "")  # 空白を削除
    print(date)
    date_list = date.split("月", 1)
    prefix = date_list[0] + "月"  # example "平成元年1月"
    suffix = date_list[1]  # example "3日（土）

    # locale.setlocale(locale.LC_ALL, 'ja_JP.UTF-8')
    # dt = datetime.strptime(suffix, '%d日（%a）')
    # dt.day  # 月の中での日にち
    # dt.weekday()  # 0-6で曜日を表す なおpythonの実装ぶっ壊れてるのであてにしてはいけない

    # return prefix, dt.day
    day = suffix.split("日", 1)

    return prefix, day


if __name__ == "__main__":
    get_detail_gonittei_url_from_top_page()
    # get_detail("http://www.kunaicho.go.jp/activity/gonittei/01/h01/gonitei-h01-01.html")
