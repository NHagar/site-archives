# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from DNAinfo_scraper.items import LinkItem 
from scrapy.spiders import Rule, CrawlSpider

class DnainfoSpider(scrapy.Spider):
    name = 'DNAinfo'
    allowed_domains = ['dnainfo.com']

    start_urls = [
            'https://www.dnainfo.com/new-york/',
            'https://www.dnainfo.com/new-york/about-us/our-team/editorial-team/',
            'https://www.dnainfo.com/chicago/',
            'https://www.dnainfo.com/chicago/about-us/our-team/editorial-team/',
            'https://www.dnainfo.com/chicago/about-us/our-team//dnainfo-staff/',
            ]

    def parse(self, response):
        for b_l in response.css('a::attr(href)').getall():
            if 'dnainfo' not in b_l:
                continue

            #if 'tags' in b_l or 'people' in b_l:
            yield scrapy.Request(response.urljoin(b_l),self.parse)

            if ('chicago/201' in b_l) or ('new-york/201' in b_l): #2012, 2013, etc.
                if b_l[:6] == '//www.':
                    b_l = 'https://www.'+b_l[6:]
                #print("Bonus link: {}".format(b_l))
                link_item = LinkItem()
                link_item['link_url'] = b_l
                yield link_item

        '''
        #link,hed,subhed,sections,byline,pub_date,html_body,text_body,tags
        outlinks = response.css('a::attr(href)').getall()
        rich_outlinks = [l for l in outlinks if '/tags/' in l or '/people/' in l]
        for l in rich_outlinks:
            if l[:6] == '//www.':
                l = 'https://www.'+l[6:]
            new_request = scrapy.Request(l)
            self.crawler.engine.crawl(new_request, self.crawler.spider)

        link = response.request.url
        hed = response.css('h1.story-headline').xpath('.//text()').get()
        subhed = ''
        sections = ''
        byline = ';'.join(response.css('a.name').xpath('.//text()').getall())
        pub_date = ''
        response.css('div.media-heading::text').get().replace("\n","")
        datetime = ''

        tags = response.css('div.googletag').xpath('@data-topic').get()
        html_body = response.css('body').get()
        text_body = ''

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
    '''

    start_urls = [
            'https://www.dnainfo.com/new-york/',
            'https://www.dnainfo.com/new-york/about-us/our-team/editorial-team/',
            'https://www.dnainfo.com/chicago/',
            'https://www.dnainfo.com/chicago/about-us/our-team/editorial-team/',
            'https://www.dnainfo.com/chicago/about-us/our-team//dnainfo-staff/',
	
            # ny neighborhoods: scrapy shell + response.xpath('//a[@data-type="Hood"]/@href').getall()
            'https://www.dnainfo.com/new-york/manhattan/chelsea-hells-kitchen',
			'https://www.dnainfo.com/new-york/manhattan/downtown',
			'https://www.dnainfo.com/new-york/manhattan/east-village-lower-east-side',
			'https://www.dnainfo.com/new-york/manhattan/greenwich-village-soho',
			'https://www.dnainfo.com/new-york/manhattan/harlem',
			'https://www.dnainfo.com/new-york/manhattan/midtown-theater-district',
			'https://www.dnainfo.com/new-york/manhattan/murray-hill-gramercy-midtown-east',
			'https://www.dnainfo.com/new-york/manhattan/upper-east-side-roosevelt-island',
			'https://www.dnainfo.com/new-york/manhattan/upper-west-side-morningside-heights',
			'https://www.dnainfo.com/new-york/manhattan/washington-heights-inwood',
			'https://www.dnainfo.com/new-york/brooklyn/bedford-stuyvesant',
			'https://www.dnainfo.com/new-york/brooklyn/cobble-hill-carroll-gardens-red-hook',
			'https://www.dnainfo.com/new-york/brooklyn/crown-heights-prospect-heights-prospect-lefferts-gardens',
			'https://www.dnainfo.com/new-york/brooklyn/fort-greene-dumbo',
			'https://www.dnainfo.com/new-york/brooklyn/park-slope-windsor-terrace-gowanus',
			'https://www.dnainfo.com/new-york/brooklyn/williamsburg-greenpoint-bushwick',
			'https://www.dnainfo.com/new-york/queens/astoria-long-island-city',
			'https://www.dnainfo.com/new-york/queens/flushing-whitestone',
			'https://www.dnainfo.com/new-york/queens/forest-hills-rego-park-jamaica',
			'https://www.dnainfo.com/new-york/queens/jackson-heights-elmhurst',
			'https://www.dnainfo.com/new-york/queens/maspeth-middle-village-ridgewood',
			'https://www.dnainfo.com/new-york/queens/rockaways',
			'https://www.dnainfo.com/new-york/bronx/fordham-tremont',
			'https://www.dnainfo.com/new-york/bronx/norwood-bedford-park',
			'https://www.dnainfo.com/new-york/bronx/riverdale-kingsbridge',
			'https://www.dnainfo.com/new-york/bronx/south-bronx',
			'https://www.dnainfo.com/new-york/bronx/woodlawn-wakefield'

            # chi neighborhoods
            'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/albany-park',
			'https://www.dnainfo.com/chicago/uptown-andersonville/andersonville',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/archer-heights',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/ashburn',
			'https://www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/auburn-gresham',
			'https://www.dnainfo.com/chicago/chicago/austin-belmont-cragin/austin',
			'https://www.dnainfo.com/chicago/logan-square-humboldt-park/avondale',
			'https://www.dnainfo.com/chicago/back-of-yards-brighton-park/back-of-yards',
			'https://www.dnainfo.com/chicago/austin-belmont-cragin/belmont-cragin',
			'https://www.dnainfo.com/chicago/beverly-mt-greenwood/beverly',
			'https://www.dnainfo.com/chicago/lakeview-wrigleyville/boystown',
			'https://www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/bridgeport',
			'https://www.dnainfo.com/chicago/back-of-yards-brighton-park/brighton-park',
			'https://www.dnainfo.com/chicago/bronzeville-washington-park/bronzeville',
			'https://www.dnainfo.com/chicago/wicker-park-bucktown/bucktown',
			'https://www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/canaryville',
			'https://www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/chatham',
			'https://www.dnainfo.com/chicago/chicago/midway-chicago-lawn-ashburn/chicago-lawn',
			'https://www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/chinatown',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/clearing',
			'https://www.dnainfo.com/chicago/bronzeville-washington-park/douglas',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/downtown',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/dunning',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/edgebrook',
			'https://www.dnainfo.com/chicago/rogers-park-edgewater/edgewater',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/edison-park',
			'https://www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/englewood',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/forest-glen',
			'https://www.dnainfo.com/chicago/garfield-park-north-lawndale/garfield-park',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/garfield-ridge',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/gladstone-park',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/gold-coast',
			'https://www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/grand-crossing',
			'https://www.dnainfo.com/chicago/south-chicago-east-side/hegewisch',
			'https://www.dnainfo.com/chicago/logan-square-humboldt-park/humboldt-park',
			'https://www.dnainfo.com/chicago/hyde-park-kenwood/hyde-park',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/irving-park',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/jefferson-park',
			'https://www.dnainfo.com/chicago/hyde-park-kenwood/kenwood',
			'https://www.dnainfo.com/chicago/lakeview-wrigleyville/lakeview',
			'https://www.dnainfo.com/chicago/lincoln-park-old-town/lincoln-park',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/lincoln-square',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/little-italy',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/little-village',
			'https://www.dnainfo.com/chicago/logan-square-humboldt-park/logan-square',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/midway',
			'https://www.dnainfo.com/chicago/beverly-mt-greenwood/morgan-park',
			'https://www.dnainfo.com/chicago/beverly-mt-greenwood/mt-greenwood',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/near-west-side',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/north-center',
			'https://www.dnainfo.com/chicago/garfield-park-north-lawndale/north-lawndale',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/north-park',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/norwood-park',
			'https://www.dnainfo.com/chicago/lincoln-park-old-town/old-town',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/pilsen',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/portage-park',
			'https://www.dnainfo.com/chicago/pullman-roseland/pullman',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/ravenswood',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/river-north',
			'https://www.dnainfo.com/chicago/rogers-park-edgewater/rogers-park',
			'https://www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/roscoe-village',
			'https://www.dnainfo.com/chicago/pullman-roseland/roseland',
			'https://www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/sauganash',
			'https://www.dnainfo.com/chicago/south-chicago-east-side/south-chicago',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/south-loop',
			'https://www.dnainfo.com/chicago/south-chicago-east-side/south-shore',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/streeterville',
			'https://www.dnainfo.com/chicago/downtown-south-loop-river-north/loop',
			'https://www.dnainfo.com/chicago/wicker-park-bucktown/ukrainian-village',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/university-village',
			'https://www.dnainfo.com/chicago/uptown-andersonville/uptown',
			'https://www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/west-lawn',
			'https://www.dnainfo.com/chicago/pilsen-little-village-near-west-side/west-loop',
			'https://www.dnainfo.com/chicago/rogers-park-edgewater/west-ridge',
			'https://www.dnainfo.com/chicago/wicker-park-bucktown/west-town',
			'https://www.dnainfo.com/chicago/wicker-park-bucktown/bucktown',
			'https://www.dnainfo.com/chicago/hyde-park-kenwood/woodlawn',
			'https://www.dnainfo.com/chicago/lakeview-wrigleyville/wrigleyville',
            ]




