import scrapy
from multiprocessing import allow_connection_pickling
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ThisClass(CrawlSpider):
    name = 'program1'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Main_Page']
    rules = (
        Rule(link_extractor=LinkExtractor(), callback='parse_page', follow=True),
    )
    
    def parse_page(self, response):
        links = response.css('links::text').get()
        para = response.css('p::text').getall()[:2]
        yield{
            'link': links,
            'para': para,
        }