from re import search

import requests
from bs4 import BeautifulSoup

headers = []
url = "https://humancostoffarmersprotest.blogspot.com/2020/12/list-of-deaths-in-farmers-protest-at.html"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')


def get_farmers_death_figure():
    for div in soup.find_all("div", class_="post-body"):
        for p in div.find_all("p"):
            total_deaths_text_line = p.get_text()
            if search("Total deaths", total_deaths_text_line):
                return total_deaths_text_line.split("=")[1].strip()


def get_farmers_death_data():
    for div in soup.find_all("div", class_="post-body"):
        for p in div.find_all("p"):
            print(p.get_text())

# def get_date_today_ymd():
 