import time
import asyncio

urls = [
    'www.1.com', 'www.2.com', 'www.3.com'
]


async def get_url(url):
    print('请求', url)
    # time.sleep(2) # time模块不支持异步
    await asyncio.sleep(2)
    print('结束', url)


tasks = []
for url in urls:
    c = get_url(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
