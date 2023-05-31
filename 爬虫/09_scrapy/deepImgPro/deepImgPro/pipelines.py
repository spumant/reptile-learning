# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class DeepimgproPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     return item
    def get_media_requests(self, item, info):
        img_src = item['img_src']
        # 请求传参，将item中的图片名称传递给file_path方法
        # meta会将自身传递给file_path
        yield scrapy.Request(url=img_src, meta={'title': item['title']})

    def file_path(self, request, response=None, info=None, *, item=None):
        # 返回图片的名称
        # 接收请求传参过来的数据
        title = request.meta['title']
        print(title, '保存下载成功')
        return title

    def item_completed(self, results, item, info):
        return item
