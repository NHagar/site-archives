'''
save-thinkprogress-info.py

A scrapy spider to collect information from thinkprogress
'''

import scrapy
import itertools
import pandas as pd

link_file = 'deduped-thinkprogress-links-only.csv'
global_start_urls = list(pd.read_csv(link_file,header=None)[0]) #[100:200] #for testing
global_start_urls = [l for l in global_start_urls if l[:8]=='https://']


class TPSpider(scrapy.Spider):
    name = 'think-progress'

    custom_settings = {
        'AUTOTHROTTLE_ENABLED' : True, #make sure set to True for big crawls
        'HTTPCACHE_ENABLED' : True,
        'ROBOTSTXT_OBEY' : True,
        'LOG_LEVEL' : 'INFO'
        # available levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
    }

    start_urls = global_start_urls
    allowed_domains = "thinkprogress.org"
    print("\n\nHello there! Starting with {} urls\n\n".format(len(global_start_urls)))

    def parse(self, response):
        #link,hed,subhed,sections,byline,pub_date,html_body,text_body,tags

        link = response.request.url
        hed = response.css('h1.post__title').xpath('.//text()').get()
        subhed = response.css('h2.post__dek').xpath('.//text()').get()
        sections = ''
        byline = response.css('span.post__byline__author').xpath('.//text()').get()
        pub_date = response.css('time.post__date').xpath('.//text()').get()
        datetime = response.css('time').xpath('@datetime').get()

        html_body = response.css('body').get()
        text_body = ''.join(response.css('div.post__content').xpath('.//text()').extract()[1:-1])
        tags = ''.join(response.css('span.tags-list').xpath('.//text()').extract()[1:-1]).replace('#','')

        yield {
            'link': link,
            'hed': hed,
            'subhed': subhed,
            'sections':sections,
            'byline':byline,
            'pub_date':pub_date,
            'datetime':datetime,
            'html_body':html_body,
            'text_body':text_body,
            'tags':tags
        }
