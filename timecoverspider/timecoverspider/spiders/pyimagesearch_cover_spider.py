import scrapy
from timecoverspider.items import MagazineCover
import datetime


class PyimagesearchCoverSpiderSpider(scrapy.Spider):
    name = "pyimagesearch_cover_spider"
    allowed_domains = ["search.time.com"]
    start_urls = ["http://search.time.com/results.html?N=46&Ns=p_date_range|1"]

    def parse(self, response):
        headers = {
            'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        url = response.css("div.refineCol ul li").xpath("a[contains(., 'TIME U.S. ')]")
        yield scrapy.Request(url.xpath("@href").extract_first(),headers = headers)