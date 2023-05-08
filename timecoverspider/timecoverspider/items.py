# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TimecoverspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MagazineCover(scrapy.Item):
    title = scrapy.Field()
    pubDate = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()