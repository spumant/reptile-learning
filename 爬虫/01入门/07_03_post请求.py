import requests

url = "https://fanyi.baidu.com/sug"
data = {
    "kw": input("请输入一个单词：")
}

resp = requests.post(url, data=data)

print(resp.json())
