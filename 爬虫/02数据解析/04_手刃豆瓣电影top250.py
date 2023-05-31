import requests
import re

f = open("top250.csv", mode="w", encoding='utf-8')
for i in range(1, 10):
    start = (i - 1) * 25
    url = "https://movie.douban.com/top250"
    data = {
        "start": start
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    resp = requests.get(url, headers=headers, params=data)
    pageSource = resp.text

    # re.S可以让正则中的点，匹配换行符
    obj = re.compile(
        r'<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
        r'.*?<p class="">.*?导演:(?P<dao>.*?)&nbsp.*?<br>'
        r'(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
        r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

    result = obj.finditer(pageSource)
    for item in result:
        name = item.group("name")
        dao = item.group("dao")
        year = item.group("year").strip()
        score = item.group("score")
        num = item.group("num")
        f.write(f"{name},{dao},{year},{score},{num}\n")

f.close()
resp.close()
print("豆瓣TOP250提取完毕")
