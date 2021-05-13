import os
from datetime import date

from lxml import etree

# import pdfkit

filename_today = date.today().strftime('%Y-%m-%d')

xml_file_name = f'../archive/{filename_today}/kirti-kisan-news-items_{filename_today}'
xml_feed_file_name = f'../archive/{filename_today}/kirti-kisan-news-items-feed_{filename_today}'


def generate_html(xml_file_name_template):
    xml_file_name = xml_file_name_template + '.xml'
    html_file_name = xml_file_name_template + '.html'
    if os.path.exists(xml_file_name):
        print('Parsing ' + xml_file_name)
        dom = etree.parse(xml_file_name)
        xslt = etree.parse('spiders/kirti-kisan-news-items.xsl')
        transform = etree.XSLT(xslt)
        newdom = transform(dom)
        with open(html_file_name, 'wb') as f:
            print('Writing '+html_file_name)
            f.write(etree.tostring(newdom, pretty_print=True))
    else:
        print('The news items xml does not exist')


if __name__ == "__main__":
    for source_xml_file in [xml_file_name , xml_feed_file_name]:
        generate_html(source_xml_file)
