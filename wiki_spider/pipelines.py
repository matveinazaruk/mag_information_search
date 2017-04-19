# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'wt')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class IdPipeline(object):
    count = 0

    def process_item(self, item, spider):
        item['id'] = self.count
        self.count += 1
        return item
