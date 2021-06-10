# Scrapy settings for tribune_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tribune_scraper'

SPIDER_MODULES = ['tribune_scraper.spiders']
NEWSPIDER_MODULE = 'tribune_scraper.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'tribune_scraper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'tribune_scraper.middlewares.TribuneScraperSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'tribune_scraper.middlewares.TribuneScraperDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'tribune_scraper.pipelines.TribuneScraperPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}
# IMAGES_STORE = 'images'
# ARCHIVE_STORE = 'D:/media/docs/personal/Dropbox/work/writings-trolleytimes/roundups/archive'

KIRTI_KEYWORDS_PA = "ਕਿਸਾਨ|ਕਿਸਾਨਾਂ|ਮਜ਼ਦੂਰ|ਮਜ਼ਦੂਰਾਂ|ਮਜਦੂਰ|ਮਜਦੂਰਾਂ|ਲੇਬਰ|ਧਰਨਾ|ਧਰਨੇ|ਯੂਨੀਅਨ|ਯੂਨੀਅਨਾਂ|ਮੋਰਚਾ|ਮੋਰਚਿਆਂ|ਕਿਰਤੀ|ਕਾਮੇ|ਪੱਲੇਦਾਰ|ਭੱਠਾ|ਮੁਲਾਜ਼ਮ|ਮੁਲਾਜਮ|ਹੜਤਾਲ|ਮੁਜ਼ਾਹਰਾ|ਵਿਰੋਧ|ਪ੍ਰਦਰਸ਼ਨ"
KIRTI_TEXT_KEYWORDS_PA = "ਕਿਸਾਨ ਮੋਰਚਾ|ਕਿਸਾਨ ਅੰਦੋਲਨ।ਕਿਸਾਨੀ ਲਹਿਰ|ਕਿਸਾਨ ਆਗੂ"
KIRTI_WOMEN_KEYWORDS_PA = "ਔਰਤ|ਔਰਤਾਂ|ਬੀਬੀ|ਬੀਬੀਆਂ|ਮਹਿਲਾ|ਮਹਿਲਾਵਾਂ|ਅਧਿਆਪਕਾ|ਅਧਿਆਪਕਾਵਾਂ|ਵਿਦਿਆਰਥਣ|ਵਿਦਿਆਰਥਣਾਂ|ਲੜਕੀ|ਲੜਕੀਆ|ਕੁੜੀ|ਕੁੜੀਆਂ"

KIRTI_KEYWORDS_HI = "किसान|किसानों|मज़दूर|मज़दूरों|मजदूर|मजदूरों|लेबर|धरना|धरने|यूनीअन|यूनीअनों|किरती|कामे"
KIRTI_TEXT_KEYWORDS_HI = "किसान मोरचा|किसान अंदोलन्।किसानी लहिर|किसान नेता"
