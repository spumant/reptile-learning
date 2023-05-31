import scrapy


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.ishuo.cn/duanzi']

    def parse(self, response):
        li_list = response.xpath('//*[@id="list"]/ul/li')
        for li in li_list:
            # 解析方法 1
            # # 得到的是一个对象，字符串数据存储在对象的data数据中
            # content = li.xpath('./div[1]/text()')[0]
            # title = li.xpath('./div[2]/a/text()')[0]
            # # 用extract方法可以取出data中的数据
            # print(title.extract())
            # print(content.extract())
            # 解析方法 2
            # title和content为列表，列表只要一个列表元素
            content = li.xpath('./div[1]/text()')
            title = li.xpath('./div[2]/a/text()')
            # extract_first()可以将列表中第0个列表元素表示的selector对象中data的参数值取出
            print(title.extract_first())
            print(content.extract_first())
