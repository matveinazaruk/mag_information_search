# coding: utf-8
from __future__ import unicode_literals

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from wiki_spider.items import WikiSpiderItem
import re


class WikiSpider(CrawlSpider):
    name = 'wiki_spider'

    start_urls = ['https://en.wikipedia.org/wiki/Los_Angeles',
                  'https://en.wikipedia.org/wiki/Information_retrieval']

    links_xpath = '(//div[@id="bodyContent"]/div/p/a)[position()<100]'
    snippet_xpath = 'string(//div[@id="bodyContent"]/div/p[1])'
    allow_re = '/wiki/' \
               '(?!((File|Talk|Category|Portal|Special|Template' \
               '|Template_talk|Wikipedia|Help|Draft):|Main_Page)).+'
    compiled_allow_re = re.compile('/wiki/'
                                   '(?!((File|Talk|Category|Portal|Special|Template'
                                   '|Template_talk|Wikipedia|Help|Draft):|Main_Page)).+')

    rules = (
        Rule(LinkExtractor(restrict_xpaths=links_xpath,
                           deny='#.*',
                           allow=allow_re),
             callback='parse_item', follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
        item = WikiSpiderItem()
        item['url'] = response.url
        item['links'] = [response.urljoin(link) for link in response.xpath(self.links_xpath).xpath('@href').extract()
                         if self.compiled_allow_re.match(link)]
        item['snippet'] = response.xpath(self.snippet_xpath).extract_first()[:255] + '...'
        return item
