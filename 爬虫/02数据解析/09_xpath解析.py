from lxml import etree

import requests

url = "https://beijing.zbj.com/search/service/?kw=saas&r=2"
resp = requests.get(url)
resp.encoding = "utf-8"

print(resp.text)

et = etree.HTML(resp.text)

divs = et.xpath('//div[@class="new-service-wrap"]/div')
for div in divs:
    price = div.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")
    if not price:
        continue
    price = price[0]
    company = div.xpath("./div/div/a[2]/div[1]/p/text()")
    name = div.xpath("./div/div/a[1]/div[2]/div[2]/p//text()")
    name = "".join(name)
    print(name, price, company)
