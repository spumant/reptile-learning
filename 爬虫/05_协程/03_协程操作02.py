import requests
import asyncio
import aiohttp
from lxml import etree

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]


def parse(t):  # 回调函数专门用于数据解析
    page_text = t.result()
    tree = etree.HTML(page_text)
    a = tree.xpath('//a[@id="feng"]/@href')[0]
    print(a)

# with前加上async
# 阻塞操作前加上 await
async def get_request(url):
    # response = await requests.get(url)
    # page_text = response.text
    async with aiohttp.ClientSession() as sess:
        async with await sess.get(url) as response:
            page_text = await response.text()
            return page_text


tasks = []
for url in urls:
    c = get_request(url)
    task = asyncio.ensure_future(c)
    task.add_done_callback(parse)
    tasks.append(task)

loop = asyncio.get_event_loop()
# asyncio.set_event_loop_policy()
loop.run_until_complete(asyncio.wait(tasks))
