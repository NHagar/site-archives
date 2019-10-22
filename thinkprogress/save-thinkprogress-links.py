'''
save-thinkprogress-links.py

A scrapy spider to collect story links from thinkprogress
'''

import scrapy
import itertools


url_template = 'https://thinkprogress.org/tag/{}/page/{}/'
tags = ['climate', 'politics', 'immigration', 'world', 'health']
max_pages = [1845, 3128, 242, 850, 810 ]

global_start_urls = []
for t,max_p in zip(tags,max_pages):
    global_start_urls += [url_template.format(t,p) for p in range(1,max_p)]


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
    print("\n\nHello there! Starting with {} urls\n\n".format(len(global_start_urls)))

    def parse(self, response):

        for quote in response.css('div.post__wrapper--inner'):
            link = quote.css('h2.post__title a::attr(href)').extract_first()
            title = quote.css('h2.post__title').xpath('.//text()').get()
            author = quote.css('span.post__byline').xpath('.//text()').get()
            date = quote.css('time').xpath('@datetime').get()
            date_pretty = quote.css('time').xpath('.//text()').get()
            #link = quote.css('a').xpath('[@rel="bookmark"]').attrib['href']

            #print("Title: {}".format(title))
            #print("Author: {}".format(author))
            #print("Date: {}".format(date_pretty))
            #print("Link: {}".format(link))
            yield {
                'title': title,
                'author': author,
                'date': date,
                'date_pretty': date_pretty,
                'link': link,
            }
