# coding: utf-8
from __future__ import unicode_literals

import scrapy


class WikiSpiderItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    links = scrapy.Field()
    snippet = scrapy.Field()
