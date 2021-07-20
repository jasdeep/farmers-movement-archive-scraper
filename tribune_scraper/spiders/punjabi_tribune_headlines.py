# -*- coding: utf-8 -*-
import os
from datetime import date
from datetime import timedelta

import pandas as pd
import scrapy
from scrapy import FormRequest

from tribune_scraper.settings import KIRTI_KEYWORDS_PA, KIRTI_WOMEN_KEYWORDS_PA, CORONA_MEDICAL_KEYWORDS_PA


class PunjabiTribuneSpider(scrapy.Spider):
    name = 'punjabi_tribune_headlines'

    start_urls = ['https://www.punjabitribuneonline.com']
    date_today_str = None
    date_today = date.today()
    filename_day = date_today.strftime('%Y-%m-%d')
    day_archive_dir = os.path.join("../data", "2020-2021")
    custom_settings = ''

    def start_requests(self):
        if self.date_today_str is not None:
            self.date_today = date.fromisoformat(self.date_today_str)
            self.filename_day = self.date_today.strftime('%Y-%m-%d')
        self.logger.info('Getting archives for the date %s', self.date_today)
        print('Getting archives for the date ', self.date_today)
        date_tomorrow = self.date_today + timedelta(days=1)
        from_date = self.date_today.strftime('%d/%m/%Y')
        to_date = date_tomorrow.strftime('%d/%m/%Y')
        return [FormRequest("https://www.punjabitribuneonline.com/archive",
                            formdata={'FromDate': from_date, 'ToDate': to_date},
                            callback=self.parse)]

    def parse(self, response, **kwargs):
        day_archive_dir = self.day_archive_dir
        try:
            os.makedirs(day_archive_dir, exist_ok=True)
        except OSError as error:
            print("Directory '%s' can not be created" % day_archive_dir)

        filename_csv = os.path.join(day_archive_dir, f'archives-page_pt_{self.filename_day}.csv')
        filename_kirti_kisan_csv = os.path.join(day_archive_dir, f'kirti-kisan-headlines_pt_{self.filename_day}.csv')
        filename_kirti_kisan_women_csv = os.path.join(day_archive_dir,
                                                      f'kirti-kisan-women_headlines_pt_{self.filename_day}.csv')
        filename_corona_medical_csv = os.path.join(day_archive_dir,
                                                   f'corona_medical_headlines_pt_{self.filename_day}.csv')

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
                        'pub_date': self.filename_day,
                        'section_title': section_title,
                        'link': "https://www.punjabitribuneonline.com" + link,
                    }
                    all_headlines.append(headline_data)
        all_headlines_df = pd.DataFrame(all_headlines, columns=['headline', 'pub_date', 'section_title', 'link'])
        all_headlines_df.to_csv(filename_csv, sep=",", index=False)
        kirti_kisan_df = all_headlines_df[all_headlines_df['headline'].str.contains(
            KIRTI_KEYWORDS_PA)]
        kirti_kisan_df.to_csv(filename_kirti_kisan_csv, index=False)
        kirti_kisan_women_df = all_headlines_df[all_headlines_df['headline'].str.contains(
            KIRTI_WOMEN_KEYWORDS_PA)]
        kirti_kisan_women_df.to_csv(filename_kirti_kisan_women_csv, index=False)
        corona_medical_df = all_headlines_df[all_headlines_df['headline'].str.contains(
            CORONA_MEDICAL_KEYWORDS_PA)]
        corona_medical_df.to_csv(filename_corona_medical_csv, index=False)
        self.logger.info('Generated csv files for the date %s', self.date_today)
        print('Generated csv files for the date ', self.date_today)
