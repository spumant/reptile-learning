import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://fanyi.baidu.com/sug']

    # 父类中的方法：该方法是用来给起始的url列表中的每一个url发请求
    def start_requests(self):
        data = {
            'kw': 'dog'
        }
        for url in self.start_urls:
            # formdata用来指定请求参数
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=data)

    def parse(self, response):
        result = response.json()
        print(result)