import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DailiSpider(CrawlSpider):
    name = 'daili'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/jianli/free.html']
    # 链接提取器：可以根据指定的规则提取链接（url）
    # 规则就是参数allow表示，allow后面跟的是正则表达式
    # link对象可以根据allow表示的正则提取到符合正则要求的链接
    link = LinkExtractor(allow=r'free_\d+\.html')
    rules = (
        # 规则解析器：该对象可以对link提取到的链接进行请求发送，然后根据制定规则解析请求到的页面源码数据
        # 此处的规则就是由callback参数来指定的
        Rule(link, callback='parse_item', follow=True),
    )
    # 数据解析
    # 该解析函数调用的次数取决于link提取链接的个数
    def parse_item(self, response):
        # item = {}
        # #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # #item['name'] = response.xpath('//div[@id="name"]').get()
        # #item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
        print(response)