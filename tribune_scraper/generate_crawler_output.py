from scrapy.crawler import CrawlerProcess

from tribune_scraper.spiders.punjabi_tribune import PunjabiTribuneSpider
from tribune_scraper.spiders.dainik_tribune import DainikTribuneSpider


process = CrawlerProcess()

process.crawl(PunjabiTribuneSpider)
process.crawl(DainikTribuneSpider)
process.start()
