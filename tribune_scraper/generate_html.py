import os
from lxml import etree

if os.path.exists('spiders/kirti-kisan-news-items_2021-05-02.xml'):
    print('Parsing news items xml')
    dom = etree.parse('spiders/kirti-kisan-news-items_2021-05-02.xml')
    xslt = etree.parse('spiders/kirti-kisan-news-items.xsl')
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    with open('kirti-kisan-news-items_2021-05-02.html', 'wb') as f:
        f.write(etree.tostring(newdom, pretty_print=True))
else:
    print('The news items xml does not exist')
