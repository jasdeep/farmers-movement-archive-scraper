<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" version="5.0" encoding="UTF-8" indent="yes"/>
    <xsl:template match="/">
        <html>
            <head>
                <link rel="stylesheet"
                      href="https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css"/>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css"/>
                <meta charset="utf-8"/>
            </head>
            <body>
                <section class="container">
                    <div class="row">
                        <div class="column column-80">
                            <h1>Punjabi Tribune Kirti Kisan News 02-05-2021</h1>
                        </div>
                    </div>
                    <xsl:for-each select="items/item">
                        <div class="row">
                            <div class="column column-80">
                                <h2>
                                    <xsl:value-of select="headline/value"/>
                                </h2>
                                <xsl:if test="not(normalize-space(subtitle/value)='')">
                                    <h3>
                                        <xsl:value-of select="subtitle/value"/>
                                    </h3>
                                </xsl:if>
                                <h4>
                                    <xsl:value-of select="pub_date"/>
                                </h4>

                                <xsl:if test="not(normalize-space(images)='')">
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
                                </xsl:if>
                                <div class="column column-75">
                                    <xsl:value-of select="text" disable-output-escaping="yes"/>
                                </div>

                                <xsl:if test="not(normalize-space(author_name)='')">
                                    <p>
                                        <strong>
                                            Author:
                                        </strong>
                                        <xsl:value-of select="author_name"/>
                                    </p>
                                </xsl:if>
                                <xsl:if test="not(normalize-space(location)='')">
                                    <p>
                                        <strong>
                                            Location:
                                        </strong>
                                        <xsl:value-of select="location"/>
                                    </p>
                                </xsl:if>
                                <xsl:if test="not(normalize-space(source_url)='')">
                                    <xsl:variable name="hyperlink">
                                        <xsl:value-of select="source_url"/>
                                    </xsl:variable>
                                    <p>
                                        <a href="{$hyperlink}">Source Link</a>
                                    </p>
                                </xsl:if>

                            </div>
                        </div>
                    </xsl:for-each>
                </section>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>