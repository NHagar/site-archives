'''
scrape-thinkprogress.py
'''

import scrapy


url_template = 'https://thinkprogress.org/tag/politics/page/{}/'


class QuotesSpider(scrapy.Spider):
    name = 'think-progress'

    custom_settings = {
        'AUTOTHROTTLE_ENABLED' : True, #set to False for big crawls
        'HTTPCACHE_ENABLED' : 'True',
        'ROBOTSTXT_OBEY' : 'True',
        'LOG_LEVEL' : 'INFO'
        # available levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
    }

    start_page = 1
    max_page = 10

    start_urls = [url_template.format(i) for i in range(start_page, max_page)]

    '''
    start_urls = [
            'https://thinkprogress.org/tag/politics/page/1/',
            'https://thinkprogress.org/tag/politics/page/2/',
    ]
    '''

    def parse(self, response):
        self.current_page = 1
        self.max_page = 10 

        #titles = response.css('.post__title').xpath('.//text()').getall()
        #bylines = response.css('.post__byline').xpath('.//text()').getall()
        for quote in response.css('div.post__wrapper--inner'):
            title = quote.css('h2.post__title').xpath('.//text()').get()
            author = quote.css('span.post__byline').xpath('.//text()').get()
            date = quote.css('time').xpath('@datetime').get()
            date_pretty = quote.css('time').xpath('.//text()').get()
            #link = quote.css('a').xpath('[@rel="bookmark"]').attrib['href']
            link = quote.css('h2.post__title a::attr(href)').extract_first()

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
