import requests
import time
from multiprocessing.dummy import Pool

start = time.time()

urls = [
    'http://127.0.0.1:5000/bobo',
    'http://127.0.0.1:5000/jay',
    'http://127.0.0.1:5000/tom'
]


def get_request(url):
    page_text = requests.get(url).text
    print(len(page_text))


pool = Pool(3)

pool.map(get_request, urls)

