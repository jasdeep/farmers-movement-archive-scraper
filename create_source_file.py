# -*- coding: utf-8 -*-
import locale
import os
import xml.etree.ElementTree as ET
from datetime import date
from datetime import datetime

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
source_text = "ਸਰੋਤ: ਸੰਯੁਕਤ ਕਿਸਾਨ ਮੋਰਚਾ, ਪੰਜਾਬੀ ਟ੍ਰਿਬਿਊਨ, ਇੰਡੀਅਨ ਐਕਸਪ੍ਰੈੱਸ"

date_today_text=date_today.strftime('%Y-%m-%d')
source_filename_path = f"tt_{date_today_text}.txt"

if not os.path.exists(source_filename_path):
    print("Creating file", source_filename_path)
    with open(source_filename_path, 'w', encoding="utf-8") as source_file:
        source_file.write(nthday_text + "\n")
        source_file.write(date_text + "\n")
        if os.path.exists(f"archive/{date_today_text}/kirti-kisan-news-items_{date_today_text}.xml"):
            parser = ET.XMLParser(encoding="utf-8")
            root = ET.parse(f"archive/{date_today_text}/kirti-kisan-news-items_{date_today_text}.xml",
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
        source_file.write("******************")
        source_file.write("\n")
        if os.path.exists(f"archive/{date_today_text}/kirti-kisan-news-items-feed_{date_today_text}.xml"):
            parser = ET.XMLParser(encoding="utf-8")
            root = ET.parse(f"archive/{date_today_text}/kirti-kisan-news-items-feed_{date_today_text}.xml",
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
