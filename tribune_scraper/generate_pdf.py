from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch

PAGESIZE = (140 * mm, 216 * mm)
BASE_MARGIN = 5 * mm


class PdfCreator:
    def add_page_number(self, canvas, doc):
        canvas.saveState()
        canvas.setFont('Times-Roman', 10)

        page_number_text = "%d" % (doc.page)
        canvas.drawCentredString(
            0.75 * inch,
            0.75 * inch,
            page_number_text
        )
        canvas.restoreState()

    def get_body_style(self):
        sample_style_sheet = getSampleStyleSheet()
        body_style = sample_style_sheet['BodyText']
        body_style.fontSize = 18
        return body_style

    def build_pdf(self):
        pdf_buffer = BytesIO()
        my_doc = SimpleDocTemplate(
            pdf_buffer,
            pagesize=PAGESIZE,
            topMargin=BASE_MARGIN,
            leftMargin=BASE_MARGIN,
            rightMargin=BASE_MARGIN,
            bottomMargin=BASE_MARGIN
        )
        body_style = self.get_body_style()
        flowables = [
            Paragraph("First paragraph", body_style),
            Paragraph(
                u"ਪਰਸ਼ੋਤਮ ਬੱਲੀ ਬਰਨਾਲਾ, 3 ਮਈ ਸੰਯੁੁਕਤ ਕਿਸਾਨ ਮੋਰਚੇ ਵੱਲੋਂ ਤਿੰਨ ਖੇਤੀ ਕਾਨੂੰਨਾਂ ਨੂੰ ਰੱਦ ਕਰਵਾਉਣ ਅਤੇ ਐੱਮਐੱਸਪੀ ਦੀ ਗਾਰੰਟੀ ਦੇਣ ਵਾਲਾ ਕਾਨੂੰਨ ਬਣਵਾਉਣ ਲਈ ਬਰਨਾਲਾ ਰੇਲਵੇ ਸਟੇਸ਼ਨ ‘ਤੇ ਲਾਇਆ ਧਰਨਾ ਅੱਜ 215ਵੇਂ ਦਿਨ ਜਿੱਥੇ ਪੂਰੇ ਜੋਸ਼ ਨਾਲ ਜਾਰੀ ਰਿਹਾ, ਉੱਥੇ ਹੀ ਧਰਨੇ ‘ਚ ਪੱਛਮੀ ਬੰਗਾਲ ‘ਚ ਭਾਜਪਾ ਦੀ ਹਾਰ ਦਾ ਮੁੱਦਾ ਕਿਸਾਨ ਸੰਘਰਸ਼ ਦੀ ਅੰਸ਼ਿਕ ਜਿੱਤ ਵਜੋਂ ਗੂੰਜਿਆ| ਇਸ ਦੌਰਾਨ ਬੁਲਾਰਿਆਂ ‘ਚ ਸ਼ਾਮਲ ਕਰਨੈਲ ਸਿੰਘ ਗਾਂਧੀ, ਯਾਦਵਿੰਦਰ ਸਿੰਘ ਚੌਹਾਨਕੇ, ਗੁੁਰਜੰਟ ਸਿੰਘ ਕਾਦੀਆਂ, ਬਾਬੂ ਸਿੰਘ ਖੁੱਡੀ ਕਲਾਂ, ਰਣਜੀਤ ਸਿੰਘ ਕਲਾਲਾ, ਨਛੱਤਰ ਸਿੰਘ ਸਾਹੌਰ, ਮੇਲਾ ਸਿੰਘ ਕੱਟੂ ਤੇ ਗੋਰਾ ਸਿੰਘ ਢਿੱਲਵਾਂ ਨੇ ਕਿਹਾ ਕਿ ਸੰਯੁੁਕਤ ਮੋਰਚੇ ਦੇ ਆਗੂ ਪੱਛਮੀ ਬੰਗਾਲ ਵਿੱਚ ਕਿਸੇ ਪਾਰਟੀ ਦੇ ਹੱਕ ਵਿੱਚ ਵੋਟਾਂ ਪਵਾਉਣ ਨਹੀਂ ਸਗੋਂ ਕੇਂਦਰੀ ਮੋਦੀ-ਸ਼ਾਹ ਹਕੂਮਤ ਵੱਲੋਂ ਪਾਸ ਕੀਤੇ ਕਾਲੇ ਖੇਤੀ ਕਾਨੂੰਨਾਂ ਦੀ ਲੋਕਮਾਰੂ ਅਸਲੀਅਤ ਦੱਸਣ ਗਏ ਸਨ, ਜਿਸ ਨੂੰ ਬੰਗਾਲ ਦੇ ਲੋਕਾਂ ਨੇ ਭਰਪੂਰ ਹੁੰਗਾਰਾ ਦਿੱਤਾ| ਆਗੂਆਂ ਨੇ ਕਿਹਾ ਕਿ ਹੁੁਣ ਪੱਛਮੀ ਬੰਗਾਲ ਦੀਆਂ ਚੋਣਾਂ ਤੋਂ ਬਾਅਦ ਬਦਲੇ ਹਾਲਾਤਾਂ ਵਿੱਚ ਸਾਡੇ ਅੰਦੋਲਨ ਨੂੰ ਹੋਰ ਬਲ ਮਿਲਿਆ ਹੈ| ਧਰਨੇ ਵਿੱਚ ਬਲਵੀਰ ਕੌਰ ਕਰਮਗੜ੍ਹ ਦੀ ਅਗਵਾਈ ਹੇਠ ਰਾਜ ਕੌਰ, ਗੁੁਰਮੇਲ ਕੌਰ, ਬਲਜੀਤ ਕੌਰ, ਮਨਜੀਤ ਕੌਰ ਤੇ ਮਹਿੰਦਰ ਕੌਰ ਦੀ ਟੀਮ ਨੇ ਆਪਣਾ ਬਿਨ-ਲਿਖਿਆ ਤਦਵਕਤੀ ਨਾਟਕ ਪੇਸ਼ ਕੀਤਾ| ਅੱਜ ਜੁੁਗਰਾਜ ਸਿੰਘ ਠੁੱਲੀਵਾਲ ਤੇ ਮੱਖਣ ਸ਼ਹਿਣਾ ਨੇ ਗੀਤ ਪੇਸ਼ ਕੀਤੇ | ਖੇਤੀ ਕਾਨੂੰਨਾਂ ਖਿਲਾਫ ਮਹਿਲ ਕਲਾਂ ਵਿੱਚ ਕਿਸਾਨਾਂ ਦਾ ਪੱਕਾ ਮੋਰਚਾ ਜਾਰੀ ਹੈ। ਇਸ ਦੌਰਾਨ ਕਿਸਾਨਾਂ ਨੇ ਕੇਂਦਰ ਸਰਕਾਰ ਖਿਲਾਫ ਨਾਅਰੇਬਾਜ਼ੀ ਕਰਦਿਆਂ ਖੇਤੀ ਕਾਨੂੰਨ ਵਾਪਸ ਲੈਣ ਦੀ ਮੰਗ ਕੀਤੀ। ਅੱਜ ਦੇ ਧਰਨੇ ਨੂੰ ਕਿਸਾਨ ਆਗੂ ਜਗਰਾਜ ਸਿੰਘ ਹਰਦਾਪੁਰਾ, ਗੁਰਮੇਲ ਸਿੰਘ ਠੁੱਲੀਵਾਲ, ਮਲਕੀਤ ਸਿੰਘ ਮਹਿਲ ਕਲਾਂ, ਕਰਮਜੀਤ ਸਿੰਘ ਗਾਂਧੀ, ਸੁਖਦੇਵ ਸਿੰਘ ਕੁਰੜ ਨੇ ਸੰਬੋਧਨ ਕਰਦਿਆਂ ਮੰਗ ਕੀਤੀ ਕਿ ਖੇਤੀ ਕਾਨੂੰਨ ਰੱਦ ਕੀਤੇ ਜਾਣ ਅਤੇ ਕਿਰਤ ਕਾਨੂੰਨਾਂ ਵਿੱਚ ਸੋਧਾਂ ਕਰਨੀਆਂ ਬੰਦ ਕੀਤੀਆ ਜਾਣ। ਕੇਂਦਰ ਸਰਕਾਰ ਵੱਲੋਂ ਪਾਸ ਖੇਤੀ ਕਾਨੂੰਨਾਂ ਖ਼ਿਲਾਫ਼ ਕਿਸਾਨ ਜਥੇਬੰਦੀਆਂ ਦਾ ਸੰਘਰਸ਼ ਕਾਫ਼ੀ ਸਮੇਂ ਤੋਂ ਜਾਰੀ ਹੈ। ਇਨ੍ਹਾਂ ਧਰਨਿਆਂ ਵਿੱਚ ਕਿਸਾਨਾਂ ਵੱਲੋਂ ਲਗਾਤਾਰ ਖੇਤੀ ਕਾਨੂੰਨ ਰੱਦ ਕਰਨ ਦੀ ਮੰਗ ਕੀਤੀ ਜਾ ਰਹੀ ਹੈ। ਅੱਜ ਦੇ ਬੁਲਾਰਿਆਂ ਵਿੱਚ ਸੁਖਪਾਲ ਸਿੰਘ ਗੋਰਖ ਨਾਥ, ਗੁਰਮੇਲ ਸਿੰਘ, ਮੰਗੂ ਸਿੰਘ ਰੰਘੜਿਆਲ, ਲੀਲਾ ਸਿੰਘ ਕਿਸਨਗੜ, ਸੁਖਦੇਵ ਸਿੰਘ, ਸੁਖਪਾਲ ਕੌਰ, ਸੁਖਵੰਤ ਕੌਰ ਖੁਡਾਲ ਸ਼ਾਮਲ ਸਨ",
                body_style)
        ]
        my_doc.build(
            flowables,
            onFirstPage=self.add_page_number,
            onLaterPages=self.add_page_number,
        )
        pdf_value = pdf_buffer.getvalue()
        pdf_buffer.close()
        return pdf_value


if __name__ == "__main__":
    pdf_creater = PdfCreator()
    pdf_response = pdf_creater.build_pdf()
    newFile = open("kirti-kisan-news-items_2021-05-04.pdf", "wb")
    newFile.write(pdf_response)
    print(pdf_response)
