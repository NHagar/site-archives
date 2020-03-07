'''
save-DNAinfo-info.py

A scrapy spider to collect information from DNA info
'''

import scrapy
import itertools
import pandas as pd
import dateutil.parser as dparser
import datefinder

#link_file = 'DNA-info-chicago-links.csv'
#link_file='DNA-info-chicago-links-https.csv'
link_file='DNA-info-new-york-links-https.csv'
global_start_urls = list(pd.read_csv(link_file,header=None)[0])# [250:300] #for testing


class InfoOnlyDNASpider(scrapy.Spider):
    name = 'DNA-info'

    custom_settings = {
        'AUTOTHROTTLE_ENABLED' : True, #make sure set to True for big crawls
        'AUTOTHROTTLE_START_DELAY' : 0.5,
        'AUTOTHROTTLE_MAX_DELAY' : 5,
        'HTTPCACHE_ENABLED' : False,
        'ROBOTSTXT_OBEY' : True,
        'LOG_LEVEL' : 'INFO',
        'ITEM_PIPELINES' : None
        # available levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
    }

    start_urls = global_start_urls
    allowed_domains = "dnainfo.com"
    print("\n\nHello there! Starting with {} urls\n\n".format(len(global_start_urls)))

    def parse(self, response):
        #link,hed,subhed,sections,byline,pub_date,html_body,text_body,tags

        link = response.request.url
        hed = response.css('h1.story-headline').xpath('.//text()').get()
        subhed = ''

        authors_and_date =' '.join(response.css('div.reporter-display').xpath('.//text()').getall())
        authors_and_date = authors_and_date.replace('&nbsp','').replace('|','')
        # the twitter handle confuses dparser
        if '@' in authors_and_date:
            authors_and_date = authors_and_date[:authors_and_date.index('@')]

        # remove the "updated" date if it exists
        if 'updated' in authors_and_date.lower():
            updated_index = authors_and_date.lower().index('updated')
            authors_and_date = authors_and_date[:updated_index]

        # parse the date finally
        # ex. 'By  Shamus Toomey   March 19, 2014 2:13pm @stoomey'
        try:
            parsed_time = dparser.parse(authors_and_date, fuzzy=True)
            fmt = '%B %d, %Y %I:%M%p'
            pub_date = parsed_time.strftime(fmt)
        except:
            pub_date = ''

        authors =''.join(response.css('div.reporter-display').xpath('.//text()').getall())
        if '|' in authors:
            date_divider_index = authors.index('|')
            authors = authors[:date_divider_index] 
        elif ' on ' in authors:
            date_divider_index = authors.index(' on ')
            authors = authors[:date_divider_index]

        authors = authors.replace('&nbsp','').replace('|','')
        authors_l = authors.split()
        if len(authors_l) > 0 and authors_l[0] == 'By':
            authors_l = authors_l[1:]
        byline = ' '.join(authors_l)

        sections = response.css('a.tag-gray').xpath('.//text()').get()

        tags = response.css('div.googletag').xpath('@data-topic').get()
        html_body = response.css('body').get()
        text_body = ''.join(response.css('article').xpath('.//p/text()').getall())

        yield {
            'link': link,
            'hed': hed,
            'subhed': subhed,
            'sections':sections,
            'byline':byline,
            'pub_date':pub_date,
            'html_body':html_body,
            'text_body':text_body,
            'tags':tags
        }
