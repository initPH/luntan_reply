# -*- coding: utf-8 -*-

# Scrapy settings for study project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'study'

SPIDER_MODULES = ['study.spiders']
NEWSPIDER_MODULE = 'study.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'study (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

COOKIE ={'oMVX_2132_saltkey': 'w9F5o6Wm', 'oMVX_2132_lastvisit': '1490101199', 'oMVX_2132_nofocus_forum': '1', 'oMVX_2132_atarget': '1', 'oMVX_2132_client_created': '1490105003', 'oMVX_2132_client_token': '345FEE508432B791138E44F9F4445B66', 'oMVX_2132_auth': '2425Yb604kwhg4Y4rriItkV%2F51uNAElV1f8vLEr3n21j3eQSwucjv%2BFg9hasdB9Mbh78Pqx75vl5r0nxyk3jAF5L5Lc', 'oMVX_2132_connect_login': '1', 'oMVX_2132_connect_uin': '345FEE508432B791138E44F9F4445B66', 'oMVX_2132_nofavfid': '1', 'oMVX_2132_forum_lastvisit': 'D_243_1490105052D_334_1490105099D_173_1490105349', 'oMVX_2132_visitedfid': '173D334D243D188', 'oMVX_2132_smile': '5D1', 'Hm_lvt_49739b392c8b45caf83863be633c629f': '1490104764,1490272511', 'Hm_lpvt_49739b392c8b45caf83863be633c629f': '1490272511', 'acw_tc': 'AQAAAPFHpEPYzQEAZd77cdngWLC0aHN2', 'oMVX_2132_lip': '222.182.102.65%2C1490105003', 'oMVX_2132_security_cookiereport': '46a1Wfepos3pNGYIxRlRtvkD%2FmwRlgVVyu4KbQnvUPwK%2F%2BFREiSw', 'oMVX_2132_onlineusernum': '608', 'oMVX_2132_ulastactivity': 'cc48c6rLdDjnV65es4RTTboV42Nsz8ByS5otqEW6s3xmR2iNhfd3', 'oMVX_2132_sendmail': '1', 'oMVX_2132_lastact': '1490272562%09forum.php%09', 'oMVX_2132_connect_is_bind': '1', 'oMVX_2132_sid': 'fo7wZo', 'Hm_lvt_8867f2e9bc13a08cafa6cffdfff2e6bd': '1490104767,1490105312,1490272514,1490272529', 'Hm_lpvt_8867f2e9bc13a08cafa6cffdfff2e6bd': '1490272529'}
#COOKIE = {'__Q_w_s_hat_seed': '1', 'RK': 'VPuO5rpLVa', 'pgv_pvi': '9715714048', 'cpu_performance_v8': '15', '__Q_w_s__QZN_TodoMsgCnt': '1', 'pgv_pvid': '6048341432', 'pt2gguin': 'o0949898050', 'uin': 'o0949898050', 'skey': '@1WJHzOif1', 'ptisp': 'ctc', 'ptcz': 'a0d01abe740fca2ac5628f3cc3e090a565a9034a894857f3cc33e9bff0b3470b', 'Loading': 'Yes', 'qzspeedup': 'sdch', 'p_skey': 'YIBGsrIPyi0EzaHG5IuZZkDf6ozXARBN8aINL*HoJmc_', 'p_uin': 'o0949898050', 'pt4_token': 'wEx5eFtrIuc3EyelseRtvCzPE-55uVLQgQqbZMP0QWM_', 'qz_screen': '1366x768', 'pgv_info': 'ssid', 'QZ_FE_WEBP_SUPPORT': '1'}
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'study.middlewares.StudySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'study.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'study.pipelines.StudyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
