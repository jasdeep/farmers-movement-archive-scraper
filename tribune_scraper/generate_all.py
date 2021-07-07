import os

import pandas as pd


def generate_historical_archive():
    for archive_date in pd.date_range('2020-06-15', '2020-09-14', freq='D'):
        os.system('scrapy crawl punjabi_tribune_headlines -a date_today_str=' + archive_date.strftime('%Y-%m-%d'))


def generate_archive_of_the_day():
    os.system('scrapy crawl punjabi_tribune')
    os.system('scrapy crawl dainik_tribune')
    os.system('python generate_html.py')
    os.system('python generate_markdown.py')
    os.system('python create_source_file.py')

if __name__=="__main__":
    generate_archive_of_the_day()