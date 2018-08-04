# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class MaoyanscrapyItem(scrapy.Item):
    name_first = scrapy.Field()
    name_second = scrapy.Field()
    url = scrapy.Field()
    movie_type = scrapy.Field()
    region_time = scrapy.Field()
    release_time = scrapy.Field()
    User_ratings = scrapy.Field()
    ratings_num = scrapy.Field()
    piao_fang = scrapy.Field()
    want_look = scrapy.Field()
    plot_introduction = scrapy.Field()
    actor = scrapy.Field()
    awards = scrapy.Field()
    comment = scrapy.Field()
