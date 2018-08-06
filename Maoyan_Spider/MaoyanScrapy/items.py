# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class MaoyanscrapyItem(scrapy.Item):

    # 电影的第一个名字
    name_first = scrapy.Field()
    # 电影的第二个名字
    name_second = scrapy.Field()
    # 电影的链接
    url = scrapy.Field()
    # 电影的类型
    movie_type = scrapy.Field()
    # 电影地区和时间
    region_time = scrapy.Field()
    # 上映时间
    release_time = scrapy.Field()
    # 用户评价
    User_ratings = scrapy.Field()
    # 评价数量
    ratings_num = scrapy.Field()
    # 累计票房
    piao_fang = scrapy.Field()
    # 想看数
    want_look = scrapy.Field()
    # 剧情介绍
    plot_introduction = scrapy.Field()
    # 主要演员
    actor = scrapy.Field()
    # 得奖
    awards = scrapy.Field()
    # 评论
    comment = scrapy.Field()
