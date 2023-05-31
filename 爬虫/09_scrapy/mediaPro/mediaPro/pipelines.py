# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


# 自定义的管道类一定要继承scrapy.pipelines中的pipeline类
class MediaproPipeline(ImagesPipeline):
    # 可以根据图片地址，对其进行请求，获取图片数据
    def get_media_requests(self, item, info):
        img_src = item['src']
        yield scrapy.Request(img_src)

    # 指定图片的存储路径：只需要返回图片存储的名称即可
    def file_path(self, request, response=None, info=None, *, item=None):
        imgName = request.url.split('/')[-1]
        print(imgName, '下载保存成功')
        return imgName

    def item_completed(self, results, item, info):
        return item  # 可以将当前的管道类接收到的item对象传递给下一个管道
