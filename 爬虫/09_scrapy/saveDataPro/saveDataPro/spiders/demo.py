import scrapy
from ..items import SavedataproItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']
    # 基于终端的持久化存储
    # def parse(self, response):
    #     li_list = response.xpath('//*[@id="list"]/ul/li')
    #     all_data = []
    #     for li in li_list:
    #         content = li.xpath('./div[1]/text()').extract_first()
    #         title = li.xpath('./div[2]/a/text()').extract_first()
    #         # extract_first()可以将列表中第0个列表元素表示的selector对象中data的参数值取出
    #         dic = {
    #             'title': title,
    #             'content': content
    #         }
    #         all_data.append(dic)
    #
    #     return all_data
    # 基于管道的持久化存储
    def parse(self, response):
        li_list = response.xpath('//*[@id="list"]/ul/li')
        all_data = []
        for li in li_list:
            content = li.xpath('./div[1]/text()').extract_first()
            title = li.xpath('./div[2]/a/text()').extract_first()
            item = SavedataproItem()
            # 通过中括号的方式访问item对象中的两个成员，且将解析到的两个字段赋值给item对象的两个成员即可
            item['title'] = title
            item['content'] = content
            yield item # 将存储好数据的item对象提交给管道
