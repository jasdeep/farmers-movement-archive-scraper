from datetime import date
from datetime import timedelta

import pandas as pd
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import FormRequest
from tribune_scraper.items import TribuneNewsItem


class PunjabiTribuneSpider(scrapy.Spider):
    name = 'punjabi_tribune'
    allowed_domains = ['www.punjabitribuneonline.com']
    SEARCH_KEYWORDS = "ਕਿਸਾਨ|ਕਿਸਾਨਾਂ|ਮਜ਼ਦੂਰ|ਮਜ਼ਦੂਰਾਂ|ਮਜਦੂਰ|ਮਜਦੂਰਾਂ|ਲੇਬਰ|ਯੂਨੀਅਨ|ਯੂਨੀਅਨਾਂ|ਮੋਰਚਾ|ਮੋਰਚਿਆਂ|ਕਿਰਤੀ"

    start_urls = ['http://www.punjabitribuneonline.com/']
    #    start_dt = date(2021, 4, 20)
    #    end_dt = date(2021, 4, 21)
    # date_today = date.today()
    date_today =  date(2021, 5, 2)
    filename_day = date_today.strftime('%Y-%m-%d')
    filename_article_counter = 0

    def start_requests(self):
        date_tomorrow = self.date_today + timedelta(days=1)
        #      from_date = self.start_dt.strftime('%d/%m/%Y')
        #      to_date = self.end_dt.strftime('%d/%m/%Y')
        from_date = self.date_today.strftime('%d/%m/%Y')
        to_date = date_tomorrow.strftime('%d/%m/%Y')
        return [FormRequest("https://www.punjabitribuneonline.com/archive",
                            formdata={'FromDate': from_date, 'ToDate': to_date},
                            callback=self.parse)]

    def parse(self, response, **kwargs):
        filename_html = f'archives-page_{self.filename_day}.html'
        filename_csv = f'archives-page_{self.filename_day}.csv'
        filename_kirti_kisan_csv = f'kirti-kisan-headlines_{self.filename_day}.csv'
        with open(filename_html, 'wb') as f:
            f.write(response.body)

        all_headlines = []
        all_pt_archive_page_sections = response.xpath('//div[@class="archive-cat-news"]')
        if all_pt_archive_page_sections:
            for pt_archive_page_section in all_pt_archive_page_sections:
                section_title = pt_archive_page_section.xpath(
                    './/div[@class="about-heading"]/h3/text()').extract_first()
                headline_links = pt_archive_page_section.xpath('.//a[@class="card-top-align"]')
                for headline_link in headline_links:
                    headline = headline_link.xpath('text()').extract_first()
                    link = headline_link.xpath('@href').extract_first()
                    headline_data = {
                        'headline': headline,
                        'link': link,
                        'section_title': section_title,
                    }
                    all_headlines.append(headline_data)
        all_headlines_df = pd.DataFrame(all_headlines, columns=['headline', 'link', 'section_title'])
        all_headlines_df.to_csv(filename_csv, sep=",", index=False)
        kirti_kisan_df = all_headlines_df[all_headlines_df['headline'].str.contains(
            self.SEARCH_KEYWORDS)]
        kirti_kisan_df.to_csv(filename_kirti_kisan_csv, index=False)
        for index, row in kirti_kisan_df.iterrows():
            absolute_url = self.start_urls[0] + row["link"]
            self.filename_article_counter += 1
            yield scrapy.Request(absolute_url, callback=self.parse_newsitem)

    def parse_newsitem(self, response):
        headline_url_text = response.url.rsplit('/', 1)[-1]
        filename_headline = headline_url_text[-8:]
        filename_kirti_kisan_newsitem = f'kirti-kisan-news_{self.filename_day}_{filename_headline}.html'
        response_body = response.body
        with open(filename_kirti_kisan_newsitem, 'wb') as f:
            f.write(response_body)

        newsitem_headline = response.xpath('//div[@class="glb-heading"]/h1/text()').get()
        newsitem_subtitle = response.xpath('//div[@class="glb-heading"]/p/text()').get()

        newsitem_image_url=response.xpath('//div[@class="news-area"]/div[@class="img-container-detail"]/img/@src').get()
        newsitem_image_caption=response.xpath('//div[@class="news-area"]/div[@class="img-container-detail"]/img/@alt').get()
        newsitem_date = response.xpath(
            '//div[@class="time-share"]/ul[1]/li[1]/p/span/text()').getall()
        newsitem_news_text_elements = response.xpath(
            '//div[@class="news-area"]/div[@class="row"]/div/div[@class="story-desc"]/p')

        newsitem_news_text_non_empty_elements = []
        newsitem_news_text_non_empty_elements_text = []
        author_name = ""
        location = ""
        for newsitem_news_text_element in newsitem_news_text_elements:
            element_text = ''
            if newsitem_news_text_element.xpath('text()').get() is not None:
                element_text = newsitem_news_text_element.xpath('text()').get()
            elif newsitem_news_text_element.xpath('strong/span/text()').get() is not None:
                element_text = newsitem_news_text_element.xpath('strong/span/text()').get()
                author_name = element_text
            elif newsitem_news_text_element.xpath('strong/text()').get() is not None:
                element_text = newsitem_news_text_element.xpath('strong/text()').get()
                if len(element_text) < 30:
                    location = element_text
            element_text_cleaned = element_text.strip()
            if element_text_cleaned != "":
                newsitem_news_text_non_empty_elements.append(newsitem_news_text_element.get())
                newsitem_news_text_non_empty_elements_text.append(element_text_cleaned)

        ##TODO

        newsitem_news_text_data = "" if newsitem_news_text_non_empty_elements is None else ' '.join(
            newsitem_news_text_non_empty_elements)

        pub_date_data = "" if newsitem_date is None else ''.join(newsitem_date).strip()
        pub_date_data_clean = " ".join(pub_date_data.split())
        tribune_news_item = TribuneNewsItem()
        tribune_news_item['headline'] = "" if newsitem_headline is None else newsitem_headline.strip(),
        tribune_news_item['subtitle'] = "" if newsitem_subtitle is None else newsitem_subtitle.strip(),
        tribune_news_item['pub_date'] = pub_date_data_clean
        tribune_news_item['text'] = newsitem_news_text_data
        tribune_news_item['author_name'] = author_name
        tribune_news_item['location'] = location
        tribune_news_item['source_url'] = response.url
        tribune_news_item['image_urls'] = newsitem_image_url
        tribune_news_item['images'] = newsitem_image_caption

        yield tribune_news_item


process = CrawlerProcess(settings={
    "FEEDS": {
        f"kirti-kisan-news-items_{PunjabiTribuneSpider.filename_day}.xml": {'format': 'xml', 'encoding': 'utf8',
                                                                            'indent': 4, },
        f"kirti-kisan-news-items_{PunjabiTribuneSpider.filename_day}.json": {
            'format': 'json',
            'encoding': 'utf8',
            'store_empty': False,
            'fields': None,
            'indent': 4,
            'item_export_kwargs': {
                'export_empty_fields': True,
            },
        },
    },
})

process.crawl(PunjabiTribuneSpider)
process.start()
