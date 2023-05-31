import requests
from bs4 import BeautifulSoup

domain = "https://www.umei.cc"
"""
注意，
    子页面的url如果开头是/，直接在前面拼上域名即可
    子页面的url不是/开头，此时需要找到主页面的url，去掉最后一个/后面的所有内容，和当前获取到的url进行拼接
"""

url = "https://www.umei.cc/tags/xinggannvshen.htm"

resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp.text)

n = 1

main_page = BeautifulSoup(resp.text, "html.parser")
a_list = main_page.find_all("a", attrs={"class": "TypeBigPics"})
for a in a_list:
    href = a.get('href')
    child_url = domain + href
    child_resp = requests.get(child_url)
    child_resp.encoding = 'utf-8'
    child_bs = BeautifulSoup(child_resp.text, "html.parser")
    div = child_bs.find("div", attrs={"class": "ImageBody"})
    img_src = div.find("img").get("src")
    img_resp = requests.get(img_src)
    with open(f"{n}.jpg", mode="wb") as f:  # 注意：此时写入到文件的是字节，所以必须是wb
        f.write(img_resp.content)
    n += 1
