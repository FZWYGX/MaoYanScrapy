# -*- coding: utf-8 -*-

# Scrapy settings for MaoyanScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MaoyanScrapy'

SPIDER_MODULES = ['MaoyanScrapy.spiders']
NEWSPIDER_MODULE = 'MaoyanScrapy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 0.75
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Host': 'maoyan.com',
    'Cookie': 'uuid_n_v=v1; uuid=A9AD4D4097B211E8926E19CBE76AC7D7DF2FFCC3E9FD47C79B70422F0E2E176C; _lxsdk_cuid=16503b12cbcc8-05ca7d0a1a1c5b-454c092b-1fa400-16503b12cbdc8; _lxsdk=A9AD4D4097B211E8926E19CBE76AC7D7DF2FFCC3E9FD47C79B70422F0E2E176C; _csrf=17982028225b48ad3b08c583e811dc1cd2765f8330403291251fa7414c0e2ae3; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=213629227.1533365267800.1533365925182.1533365926799.14; _lxsdk_s=16503b12cbd-511-2ec-938%7C%7C36',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'MaoyanScrapy.middlewares.MaoyanscrapySpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'MaoyanScrapy.middlewares.ProxyMiddleware': 200,
    'MaoyanScrapy.middlewares.UAMiddleware': 200,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'MaoyanScrapy.pipelines.MaoyanscrapyPipeline': 100,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

PROXY_URL = 'http://localhost:5555/random'

MONGODB_HOST = 'localhost'  # 本地数据库
MONGODB_PORT = '27017'  # 数据库端口
MONGODB_URI = 'mongodb://{}:{}'.format(MONGODB_HOST, MONGODB_PORT)
MONGODB_DATABASE = 'Maoyan'  # 数据库名字

SCHEDULER = "scrapy_redis.scheduler.Scheduler"  # 必有项：更改去重对列

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 必有项：利用Redis去重

SCHEDULER_PERSIST = True

REDIS_URL = 'redis://127.0.0.1:6379'  # 配置连接
