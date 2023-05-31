import requests
from lxml import etree
import ip_pond

url = "https://galaxias-api.lingxigames.com/ds/ajax/endpoint.json"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "referer": "https://sgzzqb.lingxigames.com/"
}

data = {
    "gameId": "10000175",
    "tbId": "731923860067381254"
}

proxy_list = ip_pond.get_ip(2)

resp = requests.post(url, headers=headers, proxies=proxy_list, data=data)

print(resp.text)
