# -*- coding: utf-8 -*-
import locale
import os
import shutil
import xml.etree.ElementTree as ET
from datetime import date
from datetime import datetime

from utils import get_farmers_death_figure

try:
    locale.setlocale(locale.LC_ALL, "pa_IN")
except Exception:
    try:
        locale.setlocale(locale.LC_ALL, 'pa_Guru')
    except Exception as e:
        print('An error occurred: {0}'.format(e))

date_today = datetime.today()

d0 = date(2020, 11, 26)
d1 = date_today.date()
delta = d1 - d0
nthday_text = str(delta.days) + " ਵਾਂ ਦਿਨ"
date_text = date_today.strftime("%d %B")
death_figure_text = "ਸ਼ਹੀਦ " + get_farmers_death_figure()
source_text = "ਸਰੋਤ: ਸੰਯੁਕਤ ਕਿਸਾਨ ਮੋਰਚਾ, ਪੰਜਾਬੀ ਟ੍ਰਿਬਿਊਨ, ਦੈਨਿਕ ਟ੍ਰਿਬਿਊਨ"

date_today_text = date_today.strftime('%Y-%m-%d')
source_filename_path = f"../archive/{date_today_text}/tt_{date_today_text}.txt"
source_all_filename_path = f"../archive/{date_today_text}/tt_{date_today_text}_all.txt"

if not os.path.exists(source_filename_path):
    print("Creating file", source_filename_path)
    with open(source_filename_path, 'w', encoding="utf-8") as source_file:
        source_file.write(nthday_text + "\n")
        source_file.write(date_text + "\n")
        source_file.write(death_figure_text + "\n")
        if os.path.exists(f"../archive/{date_today_text}/kirti-kisan-news-items_pt_{date_today_text}.xml"):
            parser = ET.XMLParser(encoding="utf-8")
            root = ET.parse(f"../archive/{date_today_text}/kirti-kisan-news-items_pt_{date_today_text}.xml",
                            parser=parser).getroot()
            for item in root.findall('item'):
                headline = []
                headline_text = item.find('.//headline').text
                subtitle_text = item.find('.//subtitle').text
                location_text = item.find('.//location').text
                if location_text is not None:
                    location_value = location_text if ',' not in location_text else location_text.split(',')[0]
                    headline.append(location_value + ": ")
                headline.append(headline_text)
                if subtitle_text is not None:
                    headline.append(" // " + subtitle_text.replace('*', '').strip())

                source_file.write("\n")
                source_file.write("* " + ''.join(headline))
                source_file.write("\n")
        source_file.write("\n")
        source_file.write("******************")
        source_file.write("\n")
        if os.path.exists(f"../archive/{date_today_text}/kirti-kisan-news-items_dt_{date_today_text}.xml"):
            parser = ET.XMLParser(encoding="utf-8")
            root = ET.parse(f"../archive/{date_today_text}/kirti-kisan-news-items_dt_{date_today_text}.xml",
                            parser=parser).getroot()
            for item in root.findall('item'):
                headline = []
                headline_text = item.find('.//headline').text
                subtitle_text = item.find('.//subtitle').text
                headline.append(headline_text)
                if subtitle_text is not None:
                    headline.append(" // " + subtitle_text.replace('*', '').strip())

                source_file.write("\n")
                source_file.write("* " + ''.join(headline))
                source_file.write("\n")
        source_file.write("\n")

        source_file.write(source_text + "\n")

else:
    print("File already exists", source_filename_path)

print("Copying " + source_filename_path + " to " + source_all_filename_path)
shutil.copy2(source_filename_path, source_all_filename_path)
