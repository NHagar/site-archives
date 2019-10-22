# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class DnainfoScraperPipeline(object):
    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        if item['link_url'] in self.links_seen:
            raise DropItem("Duplicate link found: {}".format(item['link_url']))
        else:
            self.links_seen.add(item['link_url'])
            return item
