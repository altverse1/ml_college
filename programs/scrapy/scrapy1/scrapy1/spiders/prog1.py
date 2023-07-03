import scrapy

class collegesite(scrapy.Spider):
    name = 'prog1'
    start_urls = ['https://nmamit.nitte.edu.in/']
    custom_settings = {
        'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    def parse(self, response):
        imgs = response.css('img::attr(src)').getall()
        paras = response.css('p::text').getall()
        
        with open('imgs.txt', mode='w', newline='') as file:
            for img in imgs:
                file.write(img+'\n')
        with open('paras.txt', mode='w', newline='') as file:
            for para in paras:
                file.write(para+'\n')
