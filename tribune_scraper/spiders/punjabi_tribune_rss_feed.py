from datetime import date
from re import search

import scrapy

from tribune_scraper.items import TribuneNewsItem
from tribune_scraper.settings import KIRTI_KEYWORDS


class PunjabiTribuneRSSFeedSpider(scrapy.Spider):
    name = 'punjabi_tribune_rss_feed'



    start_urls = ['https://www.punjabitribuneonline.com/rss/feed?catId=42',
                  'https://www.punjabitribuneonline.com/rss/feed?catId=45',
                  'https://www.punjabitribuneonline.com/rss/feed?catId=265',
                  'https://www.punjabitribuneonline.com/rss/feed?catId=218',
                  "https://www.punjabitribuneonline.com/rss/feed?catId=57",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=50",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=19",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=0",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=25",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=26",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=210",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=270",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=17",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=18",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=20",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=24",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=34",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=40",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=213",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=269",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=265",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=267",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=268",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=60",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=59",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=62",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=216",
                  "https://www.punjabitribuneonline.com/rss/feed?catId=221"
                  ]

    date_today = date.today()
    date_day_text = date_today.strftime('%d %B %Y')
    filename_day = date_today.strftime('%Y-%m-%d')

    custom_settings = {'FEEDS': {
        f'../archive/{filename_day}/kirti-kisan-news-items-feed_{filename_day}.json': {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'indent': 4,
            'item_export_kwargs': {
                'export_empty_fields': True,
            },
            'overwrite': True,
        },
        f'../archive/{filename_day}/kirti-kisan-news-items-feed_{filename_day}.xml': {
            'format': 'xml',
            'encoding': 'utf8',
            'indent': 8,
            'overwrite': True,
        },
    }
    }

    def start_requests(self):
        for url in self.start_urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for post in response.xpath('//channel/item'):
            pub_date = post.xpath('pubDate//text()').get()
            title = post.xpath('title//text()').get()
            description = post.xpath('description//text()').get()
            subtitle = "" if post.xpath('excerpt') is None else post.xpath('excerpt//text()').get()
            if date.today().strftime('%d %B %Y') in pub_date and (search(KIRTI_KEYWORDS, title) or search(
                    KIRTI_KEYWORDS, description)):
                tribune_news_item = TribuneNewsItem()
                tribune_news_item['headline'] = title
                tribune_news_item['subtitle'] = subtitle
                tribune_news_item['pub_date'] = pub_date
                tribune_news_item['text'] = description
                # tribune_news_item['text_plain'] = newsitem_news_text_plain
                # tribune_news_item['author_name'] = author_name
                # tribune_news_item['location'] = location
                tribune_news_item['source_url'] = post.xpath('link//text()').get()
                tribune_news_item['image_urls'] = post.xpath('thumbimage/text()').get()
                tribune_news_item['images'] = post.xpath('imagecaption/text()').get()
                yield tribune_news_item
