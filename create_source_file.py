# -*- coding: utf-8 -*-
import os
import locale
from datetime import datetime
from datetime import date

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

source_filename_path = date_today.strftime('%Y-%m-%d') + ".txt"

if not os.path.exists(source_filename_path):
    print("Creating file", source_filename_path)
    with open(source_filename_path, 'w', encoding="utf-8") as source_file:
        source_file.write(nthday_text + "\n")
        source_file.write(date_text + "\n")
        source_file.write("\n")
        source_file.write("*")
        source_file.write("\n")
        source_file.write("*")
        source_file.write("\n")
        source_file.write("*")
        source_file.write("\n")
        source_file.write(source_text + "\n")
else:
    print("File already exists", source_filename_path)
