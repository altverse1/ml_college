from multiprocessing import allow_connection_pickling
import scrapy
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor

class colleges(CrawlSpider):
    name = 'scrap2'
    start_urls = ['https://nmamit.nitte.edu.in/']
    rules=(Rule(LinkExtractor(),callback='parse_page', follow=True),)
    
    def parse_page(self, response):
        text = response.css('title::text').get()
        para = response.css('p::text').getall()[:2]
        yield{
            'title':text,
            'paras':para,
        }