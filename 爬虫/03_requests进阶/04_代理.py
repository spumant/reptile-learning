import requests

url = "http://www.baidu.com"
proxy = {
    "http": "",
    "https": ""
}
resp = requests.get(url,proxies=proxy)
print(resp.text)
