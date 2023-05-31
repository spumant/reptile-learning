# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddleproSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # 类方法：作用是返回一个下载器对象
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 拦截处理所有的请求对象
    # 参数：request就是拦截到的请求对象，spider是爬虫文件中爬虫类实例化的对象
    # spider参数的作用可以实现爬虫类和中间类的数据交互
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'xxx'
        request.cookies = 'xxx'
        print(request.url, ":请求对象拦截成功！")
        return None

    # 拦截处理所有的响应对象
    # 参数：response就是拦截到的响应对象，request就是被拦截到响应对象对应唯一的一个请求对象
    def process_response(self, request, response, spider):
        print(request.url, ":响应对象拦截成功！")
        return response

    # 拦截和处理发生异常的请求对象
    # 参数：request就是拦截到的发生异常的请求对象
    # 方法存在的意义：将发生异常的请求拦截到，然后对其进行修正
    def process_exception(self, request, exception, spider):
        print(request.url, ":发生异常的请求对象被拦截到！")
        # 修正操作

        # 只有发生了异常请求才使用代理机制，则可以写在该方法中
        request.meta['proxy'] = 'http://ip:port'
        return request  # 对请求对象进行重新发送
    # 控制日志输出的
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
