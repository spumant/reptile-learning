import requests
from urllib.parse import urljoin
import os
import aiohttp
import asyncio
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


async def get_ts(url):
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url, headers=headers) as response:
            ts_data = await response.read()  # 获取byte形式的响应数据
            return [ts_data, url]


def download(t):
    r_list = t.result()
    data = r_list[0]
    url = r_list[1]
    ts_name = url.split('/')[-1]
    ts_path = dirName + '/' + ts_name
    with open(ts_path, 'wb') as fp:
        fp.write(data)
    print(ts_name, "下载成功")


tasks = []
for url in ts_url_list:
    c = get_ts(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(download)
    tasks.append(task)
loop = asyncio.get_event_loop()

loop.run_until_complete(asyncio.wait(tasks))
