BOT_NAME = "wiki"

SPIDER_MODULES = ["wiki.spiders"]
NEWSPIDER_MODULE = "wiki.spiders"
ITEM_PIPELINES={'scrapy.pipelines.images.ImagesPipeline':1}
IMAGES_STORE = 'local_folder'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "wiki (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
