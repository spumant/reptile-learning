import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import CrawldemoproItem


class JianliSpider(CrawlSpider):
    name = 'jianli'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/jianli/free.html']
    # 提取页码链接
    link = LinkExtractor(allow=r'free_\d+\.html')
    # 提取简历详情页链接
    # link_detail = LinkExtractor(allow=r'https://sc.chinaz.com/jianli/\d+\.htm')
    rules = (
        # 解析每一个页码链接对应的页面数据
        Rule(link, callback='parse_item', follow=False),
        # 解析简历详情页数据
        # Rule(link_detail, callback='parse_detail', follow=False),
    )

    # 解析页码链接对应的页面数据
    def parse_item(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            title = div.xpath('./p/a/text()').extract_first()
            detail_url = div.xpath('./p/a/@href').extract_first()
            item = CrawldemoproItem()
            item['title'] = title
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

    # 解析简历详情页数据
    def parse_detail(self, response):
        item = response.meta['item']
        download_url = response.xpath('//*[@id="down"]/div[2]/ul/li[2]/a/@href').extract_first()
        item['url'] = download_url
        yield item
