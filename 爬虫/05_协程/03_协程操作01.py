import asyncio
import time


# 特殊函数
async def get_request(url):
    print(url)
    time.sleep(2)
    print("结束")
    return 123

# 回调函数的封装:必须有一个参数
def callback(t):
    # 参数t就是任务对象
    print("回调函数")
    data = t.result() # result 函数可以返回特殊函数内部的返回值
    print(data)


# 协程对象
c = get_request('www.1.com')

# 任务对象
task = asyncio.ensure_future(c)

# 给任务对象绑定回调函数
task.add_done_callback(callback)

# 事件循环对象
loop = asyncio.get_event_loop()

# 启动事件循环对象
loop.run_until_complete(task)
