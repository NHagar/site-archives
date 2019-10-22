# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from DNAinfo_scraper.items import LinkItem 
from scrapy.spiders import Rule, CrawlSpider

class DnainfoSpider(CrawlSpider):
    rules = (
            #Rule(LinkExtractor(allow=(r'.*www\.dnainfo\.com\/chicago.*',),),follow=True,callback='parse_item'),
            #Rule(LinkExtractor(allow=(r'.*www\.dnainfo\.com\/new-york.*',),),follow=True,callback='parse_item'),
            Rule(LinkExtractor(allow=(r'.*www\.dnainfo\.com\/.*',),),follow=True,callback='parse_item'),
            )


    def parse_item(self, response):
        for b_l in response.xpath('//a/@href').getall():
            if ('dnainfo.com' in b_l) and ('/201' in b_l): #2012, 2013, etc.
                #print("Bonus link: {}".format(b_l))
                link_item = LinkItem()
                link_item['link_url'] = b_l
                yield link_item

    name = 'DNAinfo'
    allowed_domains = ['dnainfo.com']
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
            'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/albany-park',
			'www.dnainfo.com/chicago/uptown-andersonville/andersonville',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/archer-heights',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/ashburn',
			'www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/auburn-gresham',
			'www.dnainfo.com/chicago/chicago/austin-belmont-cragin/austin',
			'www.dnainfo.com/chicago/logan-square-humboldt-park/avondale',
			'www.dnainfo.com/chicago/back-of-yards-brighton-park/back-of-yards',
			'www.dnainfo.com/chicago/austin-belmont-cragin/belmont-cragin',
			'www.dnainfo.com/chicago/beverly-mt-greenwood/beverly',
			'www.dnainfo.com/chicago/lakeview-wrigleyville/boystown',
			'www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/bridgeport',
			'www.dnainfo.com/chicago/back-of-yards-brighton-park/brighton-park',
			'www.dnainfo.com/chicago/bronzeville-washington-park/bronzeville',
			'www.dnainfo.com/chicago/wicker-park-bucktown/bucktown',
			'www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/canaryville',
			'www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/chatham',
			'www.dnainfo.com/chicago/chicago/midway-chicago-lawn-ashburn/chicago-lawn',
			'www.dnainfo.com/chicago/bridgeport-chinatown-mckinley-park/chinatown',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/clearing',
			'www.dnainfo.com/chicago/bronzeville-washington-park/douglas',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/downtown',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/dunning',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/edgebrook',
			'www.dnainfo.com/chicago/rogers-park-edgewater/edgewater',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/edison-park',
			'www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/englewood',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/forest-glen',
			'www.dnainfo.com/chicago/garfield-park-north-lawndale/garfield-park',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/garfield-ridge',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/gladstone-park',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/gold-coast',
			'www.dnainfo.com/chicago/englewood-auburn-gresham-chatham/grand-crossing',
			'www.dnainfo.com/chicago/south-chicago-east-side/hegewisch',
			'www.dnainfo.com/chicago/logan-square-humboldt-park/humboldt-park',
			'www.dnainfo.com/chicago/hyde-park-kenwood/hyde-park',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/irving-park',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/jefferson-park',
			'www.dnainfo.com/chicago/hyde-park-kenwood/kenwood',
			'www.dnainfo.com/chicago/lakeview-wrigleyville/lakeview',
			'www.dnainfo.com/chicago/lincoln-park-old-town/lincoln-park',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/lincoln-square',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/little-italy',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/little-village',
			'www.dnainfo.com/chicago/logan-square-humboldt-park/logan-square',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/midway',
			'www.dnainfo.com/chicago/beverly-mt-greenwood/morgan-park',
			'www.dnainfo.com/chicago/beverly-mt-greenwood/mt-greenwood',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/near-west-side',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/north-center',
			'www.dnainfo.com/chicago/garfield-park-north-lawndale/north-lawndale',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/north-park',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/norwood-park',
			'www.dnainfo.com/chicago/lincoln-park-old-town/old-town',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/pilsen',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/portage-park',
			'www.dnainfo.com/chicago/pullman-roseland/pullman',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/ravenswood',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/river-north',
			'www.dnainfo.com/chicago/rogers-park-edgewater/rogers-park',
			'www.dnainfo.com/chicago/lincoln-square-albany-park-irving-park/roscoe-village',
			'www.dnainfo.com/chicago/pullman-roseland/roseland',
			'www.dnainfo.com/chicago/jefferson-park-portage-park-norwood-park/sauganash',
			'www.dnainfo.com/chicago/south-chicago-east-side/south-chicago',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/south-loop',
			'www.dnainfo.com/chicago/south-chicago-east-side/south-shore',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/streeterville',
			'www.dnainfo.com/chicago/downtown-south-loop-river-north/loop',
			'www.dnainfo.com/chicago/wicker-park-bucktown/ukrainian-village',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/university-village',
			'www.dnainfo.com/chicago/uptown-andersonville/uptown',
			'www.dnainfo.com/chicago/midway-chicago-lawn-ashburn/west-lawn',
			'www.dnainfo.com/chicago/pilsen-little-village-near-west-side/west-loop',
			'www.dnainfo.com/chicago/rogers-park-edgewater/west-ridge',
			'www.dnainfo.com/chicago/wicker-park-bucktown/west-town',
			'www.dnainfo.com/chicago/wicker-park-bucktown/bucktown',
			'www.dnainfo.com/chicago/hyde-park-kenwood/woodlawn',
			'www.dnainfo.com/chicago/lakeview-wrigleyville/wrigleyville',
            ]




