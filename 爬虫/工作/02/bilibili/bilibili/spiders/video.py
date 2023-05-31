import scrapy
import json
from ..items import BilibiliItem


class VideoSpider(scrapy.Spider):
    name = 'video'
    # allowed_domains = ['www.xxx.com']
    start_urls = [
        'https://search.bilibili.com/all?keyword=%E6%B3%95%E5%BE%8B%E5%92%A8%E8%AF%A2&from_source=webtop_search&spm_id_from=333.1007&search_source=5'
    ]

    def parse(self, response):

        div_list = response.xpath('//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[1]/div/div')
        for div in div_list:
            video = div.xpath('./div/div[2]/a/@href').extract_first()
            video_url = "https://" + video[2:]
            # print(video_url)
            yield scrapy.Request(url=video_url, callback=self.parse_datail)

    def parse_datail(self, response):
        script = str(response.xpath('/html/head/script[3]/text()').extract_first())[20:]
        videojson = json.loads(script)
        VideoUrl = videojson['data']['dash']['video'][0]['baseUrl']
        AudioUrl = videojson['data']['dash']['audio'][0]['baseUrl']
        name = response.xpath('//*[@id="viewbox_report"]/h1/text()').extract_first()
        # print(name)
        item = BilibiliItem()
        item['name'] = name
        item['video_src'] = VideoUrl
        item['audio_src'] = AudioUrl
        yield item
