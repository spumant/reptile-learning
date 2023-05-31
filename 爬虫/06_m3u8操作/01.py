import requests
from urllib.parse import urljoin
import os
from Crypto.Cipher import AES
dirName = 'tsLib'
if not os.path.exists(dirName):
    os.mkdir(dirName)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

m1_url = "https://wolongzywcdn3.com:65/KhrLdcnW/index.m3u8"

m1_page_text = requests.get(m1_url, headers=headers).text

m1_page_text = m1_page_text.strip()

ts_url_list = []
for line in m1_page_text.split('\n'):
    if not line.startswith("#"):
        ts_url = line
        ts_url = urljoin(m1_url, ts_url)
        ts_url_list.append(ts_url)

for url in ts_url_list:
    ts_data = requests.get(url, headers=headers).content
    ts_name = url.split('/')[-1]
    ts_path = dirName + '/' + ts_name
    with open(ts_path,'wb') as fp:
        fp.write(ts_data)
