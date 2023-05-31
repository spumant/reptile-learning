import requests

url = "https://movie.douban.com/j/chart/top_list"

data = {
    "type": "13",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "10"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

resp = requests.get(url, params=data, headers=headers)

print(resp.json())
print(resp.request.url)
