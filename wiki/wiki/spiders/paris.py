import scrapy


class ParisSpider(scrapy.Spider):
    name = 'paris'
    start_urls = ['https://en.wikipedia.org/wiki/Paris']

    def parse(self, response):
        raw_image_urls = response.css('.image img ::attr(src)').getall()
        clean_image_urls=[]
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))
        
        yield {
            'image_urls': clean_image_urls
        }