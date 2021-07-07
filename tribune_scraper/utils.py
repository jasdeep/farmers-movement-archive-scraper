# -*- coding: utf-8 -*-
import json
import os
from datetime import date
from re import search

import requests
from bs4 import BeautifulSoup
from lxml import etree

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


def get_date_ymd_today():
    return get_date_ymd(date.today())


def get_date_ymd(date_object):
    return date_object.strftime('%Y-%m-%d')


def get_pt_filename_only(date_ymd=None):
    if date_ymd is None:
        date_ymd = get_date_ymd_today()
    return f'../archive/{date_ymd}/kirti-kisan-news-items_pt_{date_ymd}'


def get_dt_filename_only(date_ymd=None):
    if date_ymd is None:
        date_ymd = get_date_ymd_today()
    return f'../archive/{date_ymd}/kirti-kisan-news-items_dt_{date_ymd}'


def generate_html(output_file_name_template):
    xml_file_name = output_file_name_template + '.xml'
    html_file_name = output_file_name_template + '.html'
    if os.path.exists(xml_file_name):
        print('Parsing ' + xml_file_name)
        dom = etree.parse(xml_file_name)
        xslt = etree.parse('spiders/kirti-kisan-news-items.xsl')
        transform = etree.XSLT(xslt)
        newdom = transform(dom)
        with open(html_file_name, 'wb') as f:
            print('Writing ' + html_file_name)
            f.write(etree.tostring(newdom, pretty_print=True))
    else:
        print('The news items xml does not exist')


def generate_markdown(output_file_name_template, pub_date=None):
    if pub_date is None:
        pub_date = date.today()
    date_text = pub_date.strftime("%d %B %Y")
    json_file_name = output_file_name_template + ".json"
    markdown_file_name = output_file_name_template + ".md"
    with open(json_file_name, "r", encoding="utf-8") as read_file:
        print("Reading ", json_file_name)
        items = json.load(read_file)
        with open(markdown_file_name, "w", encoding="utf-8") as markdown_file:
            print("Writing ", markdown_file_name)
            markdown_file.write("\n")
            markdown_file.write("# News about farmers and labourers")
            markdown_file.write("\n")
            markdown_file.write("## Scraped from Punjabi Tribune")
            markdown_file.write("\n")
            markdown_file.write("## " + date_text)
            markdown_file.write("\n")
            markdown_file.write("***")
            markdown_file.write("\n")

            for item in items:
                markdown_file.write("\n")
                markdown_file.write("### " + item["headline"])
                markdown_file.write("\n")
                if item["subtitle"]:
                    markdown_file.write("#### " + item["subtitle"])
                markdown_file.write("\n")
                markdown_file.write(item["pub_date"])
                markdown_file.write("\n")

                markdown_file.write(item["text"])
                markdown_file.write("\n")
                if item["image_urls"]:
                    markdown_file.write("![" + item["images"][0] + "](" + item["image_urls"][0] + ")")
                markdown_file.write("\n")
                source_link_value = item["source_url"]
                author_location_source_text_line = "Source: [punjabitribuneonline.com](" + source_link_value + ")"
                markdown_file.write("\n")
                if item["location"]:
                    author_location_source_text_line = "Location and Date: " + item[
                        "location"] + " | " + author_location_source_text_line

                if item["author_name"]:
                    author_location_source_text_line = "Author: " + item[
                        "author_name"] + " | " + author_location_source_text_line

                markdown_file.write(author_location_source_text_line)
                markdown_file.write("\n")
                markdown_file.write("***")
                markdown_file.write("\n")

            markdown_file.write("\n")
            markdown_file.write("\n")
            markdown_file.write("##### Colophon")
            markdown_file.write("\n")
            markdown_file.write("Data scraped with Scrapy by Jasdeep Singh")
            markdown_file.write("\n")


def merge_multiple_csv_files(path, pattern):
    import os, glob
    import pandas as pd
    all_files = glob.glob(os.path.join(path, pattern))
    df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
    df_merged = pd.concat(df_from_each_file, ignore_index=True)
    df_merged.to_csv("../data/corona_medical_headlines_2020-2021.csv", index=False)


if __name__=='__main__':
    merge_multiple_csv_files("../data/2020-2021","corona_medical_headlines_pt_*.csv")