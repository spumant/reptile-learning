import requests

content = input()
url = f"https://www.sogou.com/web?query={content}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69"
}
resp = requests.get(url, headers=headers)
print(resp.text)
print(resp.request.headers)