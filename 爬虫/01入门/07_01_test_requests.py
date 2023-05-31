import requests

url = "http://www.baidu.com"
resp = requests.get(url)
resp.encoding = "utf-8"
print(resp.text)
