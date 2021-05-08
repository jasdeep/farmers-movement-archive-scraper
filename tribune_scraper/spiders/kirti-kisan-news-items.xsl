<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/">
        <html>
            <head>
                <title>ਕਿਰਤੀ ਪੰਜਾਬੀ ਟ੍ਰਿਬਿਊਨ</title>
                <link rel="stylesheet"
                      href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css"/>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
            </head>
            <body>
                <header class="container">
                    <div class="row">
                        <div class="column">
                            <p/>
                            <hr/>
                        </div>
                    </div>
                    <div class="row">
                        <div class="column">
                            <h1 style="text-align: center">ਪੰਜਾਬੀ ਟ੍ਰਿਬਿਊਨ</h1>
                            <br/>
                            <p style="text-align: center"> 6 ਮਈ 2021</p>
                            <br/>
                            <p style="text-align: center">ਅੱਜ ਦੀਆਂ ਕਿਰਤੀ ਕਿਸਾਨਾਂ ਦੀਆਂ ਖ਼ਬਰਾਂ</p>
                        </div>
                    </div>
                    <div class="row">
                        <div class="column">
                            <p/>
                            <hr/>
                        </div>
                    </div>
                </header>
                <main>
                    <xsl:for-each select="items/item">
                        <article class="container">
                            <div class="row">
                                <div class="column">
                                    <h2>
                                        <xsl:value-of select="headline"/>
                                    </h2>
                                    <xsl:if test="not(normalize-space(subtitle)='')">
                                        <h3>
                                            <xsl:value-of select="subtitle"/>
                                        </h3>
                                    </xsl:if>
                                    <h4>
                                        <xsl:value-of select="pub_date"/>
                                    </h4>
                                    <xsl:if test="not(normalize-space(text)='')">
                                        <div>
                                            <xsl:value-of select="text" disable-output-escaping="yes"/>
                                        </div>
                                    </xsl:if>
                                    <xsl:if test="not(normalize-space(image_urls)='')">
                                        <figure>
                                            <img>
                                                <xsl:attribute name="src">
                                                    <xsl:value-of select="image_urls"/>
                                                </xsl:attribute>
                                                <xsl:attribute name="title">
                                                    <xsl:value-of select="images"/>
                                                </xsl:attribute>
                                                <xsl:attribute name="alt">
                                                    <xsl:value-of select="images"/>
                                                </xsl:attribute>
                                            </img>
                                            <figcaption>
                                                <xsl:value-of select="images"/>
                                            </figcaption>
                                        </figure>
                                    </xsl:if>

                                </div>
                            </div>
                            <div class="row">
                                <xsl:if test="not(normalize-space(author_name)='')">
                                    <div class="column">
                                        <em>
                                            Author:
                                        </em>
                                        <xsl:value-of select="author_name"/>
                                    </div>
                                </xsl:if>
                                <xsl:if test="not(normalize-space(location)='')">
                                    <div class="column">
                                        <em>
                                            Location:
                                        </em>
                                        <xsl:value-of select="location"/>
                                    </div>
                                </xsl:if>
                                <xsl:if test="not(normalize-space(source_url)='')">
                                    <xsl:variable name="hyperlink">
                                        <xsl:value-of select="source_url"/>
                                    </xsl:variable>
                                    <div class="column">
                                        <a href="{$hyperlink}">Source Link</a>
                                    </div>
                                </xsl:if>
                            </div>
                            <div class="row">
                                <div class="column">
                                    <p/>
                                    <hr/>
                                </div>
                            </div>
                        </article>
                    </xsl:for-each>
                    <div class="row">
                        <div class="column">
                            <p/>
                            <hr/>
                        </div>
                    </div>
                </main>
                <footer class="container">
                    <div class="row">
                        <div class="column">
                            <p style="text-align: center">Created by scraping <a
                                    href="https://punjabitribuneonline.com/">Punjab Tribune
                            </a>  with <a href="https://scrapy.org/Scrapy">Scrapy</a> and <a
                                    href="https://www.python.org/">Python
                            </a> by
                                <a mailto="jasdeep.jogewala@gmail.com">Jasdeep Singh</a>
                            </p>
                        </div>
                    </div>
                </footer>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>