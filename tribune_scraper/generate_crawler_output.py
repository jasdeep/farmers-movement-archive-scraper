from scrapy.crawler import CrawlerProcess

from tribune_scraper.spiders.punjabi_tribune import PunjabiTribuneSpider
from tribune_scraper.spiders.punjabi_tribune_rss_feed import PunjabiTribuneRSSFeedSpider

process = CrawlerProcess()

process.crawl(PunjabiTribuneSpider)
process.crawl(PunjabiTribuneRSSFeedSpider)
process.start()
