#%%
import csv
import scrapy
import itertools
import pandas as pd
import json

#%%
with open('links.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        links = row

links = ['https://gawker.com{}'.format(i) for i in links]

with open('gawker-archive.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)

#%%
parsed_links = [i['link'] for i in obj]

#%%
remaining = list(set(links)-set(parsed_links))
remaining = [i.split('%')[0] for i in remaining]
#%%
class GSpider(scrapy.Spider):
    name = 'gawker'

    custom_settings = {
        'AUTOTHROTTLE_ENABLED' : True, #make sure set to True for big crawls
        'HTTPCACHE_ENABLED' : True,
        'ROBOTSTXT_OBEY' : True,
        'LOG_LEVEL' : 'INFO'
        # available levels: CRITICAL, ERROR, WARNING, INFO, DEBUG
    }

    start_urls = remaining
    allowed_domains = "gawker.com"
    print("\n\nHello there! Starting with {} urls\n\n".format(len(links)))

    def parse(self, response):
        #link,hed,subhed,sections,byline,pub_date,html_body,text_body,tags

        link = response.request.url
        hed = response.css('h1::text').get()
        sections = ';'.join(response.css('div.taglist > ul > li > a::text').getall())
        byline = response.css('div.meta__byline::text').get()
        pub_date = response.css('div.meta__text > time::text').get()
        html_body = response.css('div.post-content').get()
        text_body = response.css('div.post-content::text').get()
        pageviews = response.css('div.meta__pageviews::text').get()

        yield {
            'link': link,
            'hed': hed,
            'sections':sections,
            'byline':byline,
            'pub_date':pub_date,
            'html_body':html_body,
            'text_body':text_body,
            'pageviews':pageviews
        }
