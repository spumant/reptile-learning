import scrapy
from ..items import DeepimgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://pic.netbian.com/4kmeinv/']
    # 通用的url模板
    url_model = 'https://pic.netbian.com/4kmeinv/index_%d.html'
    page_num = 2

    def parse(self, response):
        # 解析出了图片名称和详情页url
        li_list = response.xpath('//*[@id="main"]/div[3]/ul/li')
        for li in li_list:
            title = li.xpath('./a/b/text()').extract_first() + '.jpg'
            detail_url = 'https://pic.netbian.com' + li.xpath('./a/@href').extract_first()
            item = DeepimgproItem()
            item['title'] = title
            # 需要对详情页的url发起请求，在详情页中获取图片的下载链接
            yield scrapy.Request(url=detail_url, callback=self.detail_parse, meta={'item': item})
        if self.page_num <= 5:
            new_url = format(self.url_model % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)

    def detail_parse(self, response):
        meta = response.meta
        item = meta['item']
        img_src = 'https://pic.netbian.com' + response.xpath('//*[@id="img"]/img/@src').extract_first()
        item['img_src'] = img_src
        yield item
