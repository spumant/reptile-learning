# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import requests
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines import ItemPipelineManager


class BilibiliPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['video_src'], meta={'name': item['name'] + '_video.mp4'})
        yield scrapy.Request(url=item['audio_src'], meta={'name': item['name'] + '_audio.mp3'})

    def file_path(self, request, response=None, info=None, *, item=None):
        filename = request.meta['name']
        return filename

    def item_completed(self, results, item, info):
        return item
    # def process_item(self, item, spider):
    #     print(item)
    #     # name = item['name']+'_video'
    #     # res = requests.get(url=item['video_src'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'})
    #     # with open(f'G:\\abc\\{name}.mp4', 'wb') as f:
    #     #     f.write(res.content)
    #     return item



