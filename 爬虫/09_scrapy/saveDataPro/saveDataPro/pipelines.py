# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SavedataproPipeline:
    # 重写父类的方法
    fp = None

    def open_spider(self, spider):
        # open_spider方法，在项目运行环节，只会被执行一次
        print('')
        self.fp = open('duanzi.txt', 'w', encoding='utf-8')

    # 用来接收爬虫文件传递过来的item对象
    # item参数，就是管道接收到的item类型对象
    # 方法调用的次数取决于爬虫的文件给其提交item的次数
    def process_item(self, item, spider):
        # item 类型的对象其实就是一个字典
        # print(item)
        title = item['title']
        content = item['content']
        self.fp.write(title + ':' + content + '\n')
        return item

    def close_spider(self, spider):
        # 在爬虫结束的时候会被执行一次
        self.fp.close()