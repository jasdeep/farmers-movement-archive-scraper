import os
import requests
import logging
import csv
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from datetime import timedelta
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from aksharamukha import transliterate

PT_URL = "https://www.punjabitribuneonline.com"
PT_ARCHIVE_URL = "{}/archive".format(PT_URL)
SEARCH_KEYWORDS = "ਕਿਸਾਨ|ਕਿਸਾਨਾਂ|ਮਜ਼ਦੂਰ|ਮਜ਼ਦੂਰਾਂ|ਮਜਦੂਰ|ਮਜਦੂਰਾਂ|ਲੇਬਰ|ਯੂਨੀਅਨ|ਯੂਨੀਅਨਾਂ|ਮੋਰਚਾ|ਮੋਰਚਿਆਂ|ਕਿਰਤੀ"

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("pt-scraper")


def scrape_archive_links_and_save_csv(soup):
    """ Scrapes article headlines and links from the HTML of archive page of the day
    """
    archive_csv_file = csv.writer(open(day_headlines_links_csv_file_name, "w", encoding="utf-8", newline=''))
    archive_csv_file.writerow(["headline", "link"])
    archive_news_divs = soup.find_all('div', class_='archive-cat-news')
    for archive_news_div in archive_news_divs:
        archive_news_links = archive_news_div.find_all('a', class_='card-top-align', href=True)
        for archive_news_link in archive_news_links:
            news_item_byline = archive_news_link.text.strip()
            news_item_link = PT_URL + archive_news_link['href']
            archive_csv_file.writerow([news_item_byline, news_item_link])


def scrape_pt_website_and_save_local_copy():
    """Gets the archives page of the day and saves it on disk"""
    response_from_pt_archive_website = requests.post(PT_ARCHIVE_URL, data=payload, verify=False)
    if response_from_pt_archive_website.status_code == 200:
        soup = BeautifulSoup(response_from_pt_archive_website.content, 'html.parser')
        with open(day_html_dump_file_name, 'a', encoding="utf-8") as archive_file:
            archive_file.write(str(soup))
        return soup
    else:
        logger.error(
            "Expected  response 200 but got: %s " % response_from_pt_archive_website.status_code)
        logger.error("PT Archive Returned: %s  " % response_from_pt_archive_website.text)


if __name__ == "__main__":
    date_today = date.today()
    date_tomorrow = date_today + timedelta(days=1)
    from_date = date_today.strftime('%d/%m/%Y')
    to_date = date_tomorrow.strftime('%d/%m/%Y')
    payload = {'FromDate': from_date, 'ToDate': to_date}
    date_today_YYYY_MM_DD_format = date_today.strftime('%Y-%m-%d')
    day_html_dump_file_name = date_today_YYYY_MM_DD_format + ".html"
    day_headlines_links_csv_file_name = date_today_YYYY_MM_DD_format + ".csv"
    day_headlines_links_csv_file_name_farmers_only = date_today_YYYY_MM_DD_format + "_farmers.csv"

    logger.info('Getting Punjabi Tribune Headlines for ' + date_today_YYYY_MM_DD_format)

    # search the website archive for a given date and save the results in an html
    if not os.path.exists(day_html_dump_file_name):
        soup = scrape_pt_website_and_save_local_copy()
    else:
        soup = BeautifulSoup(open(day_html_dump_file_name, encoding="utf-8"), 'html.parser')

    logger.info('Scrapping Punjabi Tribune headlines to ' + day_headlines_links_csv_file_name)
    # scrape the search results and save headlines and links in a csv
    if not os.path.exists(day_headlines_links_csv_file_name):
        scrape_archive_links_and_save_csv(soup)
    else:
        logger.info("headline scrapping done")

    # filter farmers only head lines
    # TODO: add more keywrods
    logger.info(
        'Filtering farmers labourer related headlines Punjabi Tribune headlines to ' + day_headlines_links_csv_file_name_farmers_only)
    if os.path.exists(day_headlines_links_csv_file_name):
        headlines_data_frame = pd.read_csv(day_headlines_links_csv_file_name)
        print(len(headlines_data_frame.index), "total headlines")
        farmers_only_headlines_data_frame = headlines_data_frame[headlines_data_frame['headline'].str.contains(
            SEARCH_KEYWORDS)]
        farmers_only_headlines_data_frame.to_csv(day_headlines_links_csv_file_name_farmers_only, index=False)

    logger.info('Reading farmers labourer related headlines')
    # read farmer articles and save
    if os.path.exists(day_headlines_links_csv_file_name_farmers_only):
        farmers_only_headlines_data_frame = pd.read_csv(day_headlines_links_csv_file_name_farmers_only)
        logger.info(str(len(farmers_only_headlines_data_frame.index)) + "farmers labourer only headlines")
        for index, row in farmers_only_headlines_data_frame.iterrows():
            headline_data = row['headline']
            link = row['link']
            response_from_pt_archive_website = requests.get(link, verify=False)
            if response_from_pt_archive_website.status_code == 200:
                soup = BeautifulSoup(response_from_pt_archive_website.content, 'html.parser')
                with open(day_html_dump_file_name, 'a', encoding="utf-8") as archive_file:
                    archive_file.write(str(soup))
            #    return soup

            # print(transliterate.process('Gurmukhi', 'RomanReadable', headline_data),
            #       row['link'])
