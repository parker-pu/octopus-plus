import scrapy


class RcsSpider(scrapy.Spider):
    name = 'rcs'
    allowed_domains = ['www.rcs.com']
    start_urls = ['http://www.rcs.com/']

    def parse(self, response):
        pass
