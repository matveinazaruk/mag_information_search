# -*- coding: utf-8 -*-

import scrapy


class WikiSpiderItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    snippet = scrapy.Field()
