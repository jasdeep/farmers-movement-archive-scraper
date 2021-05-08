# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TribuneArchiveLinkItem(scrapy.Item):
    headline = scrapy.Field()
    link = scrapy.Field()
    section = scrapy.Field()


class TribuneNewsItem(scrapy.Item):
    headline = scrapy.Field()
    subtitle = scrapy.Field()
    pub_date = scrapy.Field(serializer=str)
    section_title = scrapy.Field()
    author_name = scrapy.Field()
    location = scrapy.Field()
    text = scrapy.Field()
    text_plain = scrapy.Field()
    source_url = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
