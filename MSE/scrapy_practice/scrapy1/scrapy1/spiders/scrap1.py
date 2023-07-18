import scrapy

class collegescrapy(scrapy.Spider):
    name = 'scrap1'
    start_urls = ['https://nmamit.nitte.edu.in/']
    
    def parse(self, response):
        images = response.css('img::attr(src)').getall()
        paras = response.css('p::text').getall()
        with open('image.txt','w') as file:
            for image in images:
                file.write(image+'\n')
        with open('para.txt','w') as file:
            for para in paras:
                file.write(para+'\n')
