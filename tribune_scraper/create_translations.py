# -*- coding: utf-8 -*-
import argparse
import os
from google.cloud import translate
from datetime import date

date_today_text= date.today().strftime("%Y-%m-%d")

def google_translate_text(text="YOUR_TEXT_TO_TRANSLATE", project_id="YOUR_PROJECT_ID", source_lang="auto",
                          dest_lang="en-US"):
    """Translating Text."""

    client = translate.TranslationServiceClient()

    location = "global"

    parent = f"projects/{project_id}/locations/{location}"

    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",  # mime types: text/plain, text/html
            "source_language_code": source_lang,
            "target_language_code": dest_lang,
        }
    )

    # Display the translation for each input text provided
    for translation in response.translations:
        return translation.translated_text
        # print("Translated text: {}".format(translation.translated_text))


def translate_text(text, src="auto", dest="en"):
    project_id = "booming-post-310408"
    """Translate `text` from `src` language to `dest`"""
    return google_translate_text(text, project_id, src, dest)


def write_translated_file(source_file, src_lang, dest_lang):
    translated_text = translate_text(open(source_file, encoding="utf-8").read(), src=src_lang, dest=dest_lang)
    # write to new document file
    target_file = os.path.join(dirname, f"{filename}_{dest_lang}{f'.{ext}' if ext else ''}")
    if not os.path.exists(target_file):
        print("Creating translation file", target_file)
        open(target_file, "w", encoding="utf-8").write(
            translated_text)
    else:
        print("Translation file already exists", target_file)


if __name__ == "__main__":

    target = f'../archive/{date_today_text}/tt_{date_today_text}.txt'
    src = "pa"

    if os.path.isfile(target):
        # translate a document instead
        # get basename of file
        basename = os.path.basename(target)
        # get the path dir
        dirname = os.path.dirname(target)
        try:
            filename, ext = basename.split(".")
        except:
            # no extension
            filename = basename
            ext = ""

        # write english
        write_translated_file(target, src, "en")
        # write hindi
        write_translated_file(target, src, "hi")
        # write ur
        #write_translated_file(target, src, "ur")

#
