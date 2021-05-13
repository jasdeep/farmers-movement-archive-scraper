# -*- coding: utf-8 -*-
import locale
from datetime import date

from mdutils.mdutils import MdUtils

try:
    locale.setlocale(locale.LC_ALL, "pa_IN")
except Exception:
    try:
        locale.setlocale(locale.LC_ALL, 'pa_Guru')
    except Exception as e:
        print('An error occurred: {0}'.format(e))

date_text = date.today().strftime("%d %B %Y")

filename_day = date.today().strftime('%Y-%m-%d')
file_name = f'../archive/{filename_day}/kirti-kisan-news-items_{filename_day}'
json_file_name = file_name + ".json"
md_file_name = file_name + ".md"

mdFile = MdUtils(file_name=file_name, title='ਪੰਜਾਬੀ ਟ੍ਰਿਬਿਊਨ')

mdFile.new_header(level=2, title=date_text)
mdFile.new_header(level=3, title='ਅੱਜ ਦੀਆਂ ਕਿਰਤੀ ਕਿਸਾਨਾਂ ਦੀਆਂ ਖ਼ਬਰਾਂ')

mdFile.new_header(level=3, title='ਕਿਸਾਨ ਜਥੇਬੰਦੀਆਂ ਵੱਲੋਂ ਲੌਕਡਾਊਨ ਦਾ ਵਿਰੋਧ ਅੱਜ')

mdFile.new_paragraph(
    "ਮਨਧੀਰ ਸਿੰਘ ਦਿਓਲ ਨਵੀਂ ਦਿੱਲੀ, 7 ਮਈ ਕੇਂਦਰ ਸਰਕਾਰ ਵੱਲੋਂ ਦੇਸ਼ ’ਚ ਕਰੋਨਾ ਦੇ ਵੱਧ ਰਹੇ ਮਰੀਜ਼ਾਂ ਦੇ ਮੱਦੇਨਜ਼ਰ ਵੱਖ-ਵੱਖ ਸੂਬਿਆਂ ਵਿੱਚ ਲਾਗੂ ਕੀਤੇ ਗਏ ਲੌਕਡਾਊਨ ਦੇ ਚੱਲਦਿਆਂ ਪੰਜਾਬ ਸਰਕਾਰ ਵੱਲੋਂ ਵੀ ਲੌਕਡਾਊਨ ਲਾਉਣ ਦੇ ਵਿਰੋਧ ਵਿੱਚ ਪੰਜਾਬ ਦੀਆਂ 32 ਕਿਸਾਨ ਜਥੇਬੰਦੀਆਂ ਨੇ 8 ਮਈ ਨੂੰ ਲੌਕਡਾਊਨ ਦੇ ਵਿਰੋਧ ਦਾ ਐਲਾਨ ਕੀਤਾ ਹੈ। ਕਿਸਾਨ ਆਗੂ ਡਾ. ਦਰਸ਼ਨ ਪਾਲ ਨੇ ਕਿਹਾ ਕਿ ਸਰਕਾਰ ਕਰੋਨਾ ਬਿਮਾਰੀ ਤੋਂ ਬਚਾਅ ਲਈ ਡਾਕਟਰਾਂ, ਦਵਾਈਆਂ, ਹਸਪਤਾਲਾਂ ਦਾ ਪ੍ਰਬੰਧ ਕਰਨ ਦੀ ਥਾਂ ਲੋਕਾਂ ਨੂੰ ਜਬਰੀ ਘਰਾਂ ’ਚ ਕੈਦ ਕਰ ਰਹੀ ਹੈ ਤੇ ਦੁਕਾਨਦਾਰਾਂ ਦੀਆਂ ਦੁਕਾਨਾਂ ਜਬਰੀ ਬੰਦ ਕਰਵਾ ਰਹੀ ਹੈ। ਇਸ ਕਾਰਨ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਸਾਲ ਦੇ ਘਾਟੇ ਦਾ ਸ਼ਿਕਾਰ ਦੁਕਾਨਦਾਰ ਮਰਨ ਕੰਢੇ ਖੜ੍ਹੇ ਹਨ। ਉਨ੍ਹਾਂ ਕੋਲ ਭੁੱਖੇ ਮਰਨ ਜਾਂ ਫਿਰ ਸੰਘਰਸ਼ ਕਰਨ ਤੋਂ ਬਿਨਾਂ ਕੋਈ ਚਾਰਾ ਨਹੀਂ ਰਿਹਾ ਹੈ। ਜਗਮੋਹਨ ਸਿੰਘ ਨੇ ਕਿਹਾ ਕਿ ਸਰਕਾਰ ਨੇ ਸਰਕਾਰ ਕਿਸਾਨੀ ਅੰਦੋਲਨ ਨੂੰ ਖਤਮ ਕਰਨ ਲਈ ਲਾਕਡਾਊਨ ਲਗਾ ਰਹੀ ਹੈ ਤਾਂ ਜੋ ਕਰੋਨਾ ਤੋਂ ਡਰਦੇ ਲੋਕ ਘਰਾਂ ਅੰਦਰ ਕੈਦ ਹੋ ਜਾਣ ਅਤੇ ਦਿੱਲੀ ਦੀਆਂ ਹੱਦਾਂ ’ਤੇ ਲੱਗੇ ਮੋਰਚੇ  ਖਾਲੀ ਹੋ ਜਾਣ ਤੇ ਇਸ ਕੰਮ ਵਿੱਚ ਕੈਪਟਨ ਸਰਕਾਰ, ਮੋਦੀ ਸਰਕਾਰ ਨਾਲ ਰਲੀ ਹੋਈ ਹੈ। ਉਨ੍ਹਾਂ ਕਿਹਾ ਕਿ ਇਸ ਦਾ ਡੱਟਵਾਂ ਵਿਰੋਧ ਕਰਦੇ ਹੋਏ ਦੁਕਾਨਦਾਰਾਂ ਨੂੰ ਉਨ੍ਹਾਂ ਦਾ ਸੁਨੇਹਾ ਹੈ ਕਿ ਪ੍ਰਸ਼ਾਸਨ ਦੇ ਕਿਸੇ ਵੀ ਝਾਂਸੇ ’ਚ ਆਉਣ ਦੀ ਥਾਂ ਸਾਰਾ ਹਫ਼ਤਾ ਤੇ ਸਾਰਾ ਦਿਨ ਹਰ ਤਰ੍ਹਾਂ ਦੀਆਂ ਦੁਕਾਨਾਂ ਖੋਲ੍ਹ ਕੇ ਰੱਖੀਆਂ ਜਾਣ। ਇਸ ਲਈ ਜਥੇਬੰਦੀਆਂ ਹਰ ਮਦਦ ਕਰਨਗੀਆਂ। ਸੰਤੋਖ ਸਿੰਘ ਸੰਧੂ ਨੇ ਕਿਹਾ ਕਿ ਕਰੋਨਾ ਸੰਕਟ ਦੇ ਨਾਂ ’ਤੇ ਜਬਰੀ ਥੋਪੇ ਲੌਕਡਾਊਨ ਕਾਰਨ ਸ਼ਹਿਰੀ ਕਾਰੋਬਾਰੀਆਂ, ਮਜ਼ਦੂਰਾਂ ਤੇ ਪੇਂਡੂ ਲੋਕਾਂ ਨੂੰ ਭਾਰੀ ਆਰਥਿਕ ਮੁਸ਼ਕਲਾਂ ਦਾ ਸਾਹਮਣਾ ਕਰਨਾ ਪੈ ਰਿਹਾ ਹੈ। ਕੈਪਟਨ ਸਰਕਾਰ ਕਰੋਨਾ ਦੀ ਰੋਕਥਾਮ ਲਈ ਵਿਗਿਆਨਕ ਢੰਗ ਅਪਣਾਉਣ, ਲੋੜੀਂਦੀਆਂ ਮੈਡੀਕਲ ਸਹੂਲਤਾਂ ਦੇਣ ਦੀ ਥਾਂ ਲੋਕਾਂ ਨੂੰ ਜਬਰੀ ਘਰਾਂ ਅੰਦਰ ਕੈਦ ਕਰਕੇ ਦਹਿਸ਼ਤ ਪੈਦਾ ਕਰ ਰਹੀ ਹੈ। ਸ਼ਹਿਰੀ ਕਾਰੋਬਾਰੀਆਂ ਤੇ ਉਨ੍ਹਾਂ ਦੇ ਹੱਕ ਵਿੱਚ ਜਥੇਬੰਦੀਆਂ ਵੱਲੋਂ ਆਵਾਜ਼ ਬੁਲੰਦ ਕਰਨ ਤੋਂ ਬਾਅਦ ਭਾਵੇਂ ਸਰਕਾਰ ਨੂੰ ਬਹੁਤ ਸਾਰੇ ਕਾਰੋਬਾਰੀ ਅਦਾਰੇ ਸੀਮਤ ਸਮੇਂ ਲਈ ਖੋਲ੍ਹਣ ਦੀ ਇਜਾਜ਼ਤ ਦੇਣੀ ਪਈ ਹੈ ਪਰ ਦੂਜੇ ਪਾਸੇ ਬੇਲੋੜੀਆਂ ਰੋਕਾਂ ਲਾ ਕੇੇ ਖੌਫ ਪੈਦਾ ਕਰਨ ਦੀ ਸਾਜ਼ਿਸ਼ ਰਚੀ ਜਾ ਰਹੀ ਹੈ। ਆਗੂਆਂ ਕਿਹਾ ਕਿ ਬਰਨਾਲਾ ਜ਼ਿਲ੍ਹੇ ਅੰਦਰ ਇੱਕੋ ਇੱਕ ਸਰਕਾਰੀ ਹਸਪਤਾਲ ਵਿੱਚ ਸਾਲ ਭਰ ਪਹਿਲਾਂ ਆਏ ਵੈਂਟੀਲੇਟਰ ਚਿੱਟੇ ਹਾਥੀ ਬਣੇ ਹੋਏ ਹਨ। ਮਨਜੀਤ ਸਿੰਘ ਰਾਏ ਨੇ ਕਿਹਾ ਕਿ ਕਰੋਨਾਵਾਇਰਸ ਦੇ ਨਾਂ ’ਤੇ ਸਰਕਾਰ ਸ਼ਾਹੀਨ ਬਾਗ ਵਾਂਗ ਕਿਸਾਨੀ ਸੰਘਰਸ਼ ਨੂੰ ਵੀ ਖਤਮ ਕਰਨਾ ਚਾਹੁੰਦੀ ਹੈ। ਕੇਂਦਰ ਤੇ ਸੂਬਾ ਸਰਕਾਰਾਂ ਛੋਟੇ ਕਾਰੋੋਬਾਰੀਆਂ ਤੇ ਕਿਰਤੀਆਂ ਦਾ ਉਜਾੜਾ ਕਰਨ ’ਤੇ ਤੁਲੀਆਂ ਹੋਈਆਂ ਹਨ। ਕਸ਼ਮੀਰ ਸਿੰਘ ਨੇ ਕਿਹਾ ਕਿ ਜਬਰੀ ਥੋਪੇ ਲੌਕਡਾਊਨ ਖ਼ਿਲਾਫ਼ ਸਾਰੀਆਂ ਇਕਾਈਆਂ ਸ਼ਹਿਰੀ ਕਾਰੋਬਾਰੀਆਂ ਦਾ ਡਟਵਾਂ ਸਾਥ ਦੇਣ। ਕਣਕ ਦੀ ਵਾਢੀ ਦਾ ਕੰਮ ਖਤਮ ਹੋ ਗਿਆ ਹੈ। ਸਮੁੱਚੇ ਕਿਸਾਨ ਤੇ ਹੋਰ ਲੋਕ ਸੰਘਰਸ਼ ਨੂੰ ਮਜ਼ਬੂਤ ਕਰਨ। ਸੰਘਰਸ਼ ਵਿੱਚ ਔਰਤਾਂ ਸਮੇਤ ਨੌਜਵਾਨਾਂ ਦੀ ਸ਼ਮੂਲੀਅਤ ਯਕੀਨੀ ਬਣਾਈ ਜਾਵੇ।"
    )

mdFile.create_md_file()

# ਅੱਜ ਦੀਆਂ ਕਿਰਤੀ ਕਿਸਾਨਾਂ ਦੀਆਂ ਖ਼ਬਰਾਂ