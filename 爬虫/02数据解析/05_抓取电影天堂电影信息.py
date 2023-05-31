import requests
import re

url = "https://www.dy2018.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)

resp.encoding = 'gbk'
pageSource = resp.text

obj1 = re.compile(r"2023必看热片.*?<ul>(?P<html>.*?)</ul>", re.S)
result1 = obj1.search(pageSource)

html = result1.group("html")
# print(html)

obj2 = re.compile(r"<li><a href='(?P<href>.*?)' title")
result2 = obj2.finditer(html)

obj3 = re.compile(r'<div id="Zoom">.*?◎片　　名(?P<movie>.*?)<br />.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

for item in result2:
    child_url = url.strip('/') + item.group("href")
    child_resp = requests.get(child_url)
    child_resp.encoding = 'gbk'
    result3 = obj3.search(child_resp.text)
    movie = result3.group("movie")
    download = result3.group("download")
    print(movie, download)
