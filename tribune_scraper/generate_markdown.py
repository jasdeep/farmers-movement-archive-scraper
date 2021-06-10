# -*- coding: utf-8 -*-
import json
import locale
from datetime import date

try:
    locale.setlocale(locale.LC_ALL, "pa_IN")
except Exception:
    try:
        locale.setlocale(locale.LC_ALL, 'pa_Guru')
    except Exception as e:
        print('An error occurred: {0}'.format(e))

date_text = date.today().strftime("%d %B %Y")

filename_day = date.today().strftime('%Y-%m-%d')
file_name = f'../archive/{filename_day}/kirti-kisan-news-items_pt_{filename_day}'
json_file_name = file_name + ".json"
markdown_file_name = file_name + ".md"
pdf_file_name = file_name + ".pdf"
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

# with open(markdown_file_name, 'r', encoding="utf-8") as markdown_file_text:
#   html_text = markdown(markdown_file_text.read(), output_format='html4')
# print("Writing", pdf_file_name)
# pdfkit.from_string(html_text, pdf_file_name)
