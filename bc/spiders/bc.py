# -*- coding: utf-8 -*-
from scrapy.exceptions import DontCloseSpider
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import signals


class BCSpider(CrawlSpider):
    name = 'bc'

    rules = (
       Rule(LinkExtractor(), follow=True),
    )

    def __init__(self, *args, **kwargs):
        super(BCSpider, self).__init__(*args, **kwargs)
        self._follow_links = True

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(BCSpider, cls).from_crawler(crawler, *args, **kwargs)
        spider._set_crawler(crawler)
        spider.crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        return spider

    def spider_idle(self):
        self.log("Spider idle signal caught.")
        raise DontCloseSpider
