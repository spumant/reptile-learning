# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import redis
import pymongo


class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='monarch99',
            db='spider3qi',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        title = item['title']
        sql = 'insert into xiaoshuo(title) values ("%s")' % title
        self.cursor.execute(sql)
        self.conn.commit()
        return item


class RedisPipeLine:
    conn = None

    def open_spider(self, spider):
        self.conn = redis.Redis(
            host='127.0.0.1',
            port=6379
        )

    def process_item(self, item, spider):
        # 如果想将一个字典直接存入redis中，则redis模块的版本一定要是2.10.6
        self.conn.lpush('xiaoshuo', item['title'])
        return item

    def close_spider(self, spider):
        self.conn.close()


class MongoPipeline:
    conn = None
    db_sanqi = None

    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(
            host='127.0.0.1',
            port=27017
        )
        self.db_sanqi = self.conn['sanqi']

    def process_item(self, item, spider):
        self.db_sanqi['xiaoshuo'].insert_one({'title': item['title']})
        return item
