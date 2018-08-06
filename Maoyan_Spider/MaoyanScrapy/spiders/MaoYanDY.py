# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from traceback import format_exc
from scrapy import Selector
from ..Utils_model.font import font_creator
from ..items import MaoyanscrapyItem


class MaoyandySpider(scrapy.Spider):
    name = 'MaoYanDY'
    allowed_domains = ['maoyan.com', 'api.xdaili.cn', 'xdaili-api']

    start_urls = ['http://maoyan.com/films?showType=3',
                  'http://maoyan.com/films?showType=2',
                  'http://maoyan.com/films?showType=1']

    def parse(self, response):
        movie_type = response.xpath('//*[@id="app"]/div/div[1]/ul/li[1]/ul/li/a/@href').extract()
        movie_type = movie_type[1:]
        print(movie_type)

        movie_region = response.xpath('//*[@id="app"]/div/div[1]/ul/li[2]/ul/li/a/@href').extract()
        movie_region = movie_region[1:]
        print(movie_region)

        movie_time = response.xpath('//*[@id="app"]/div/div[1]/ul/li[3]/ul/li/a/@href').extract()
        movie_time = movie_time[1:]
        print(movie_time)

        for x in movie_type:
            index_x_url = 'http://maoyan.com/films' + str(x)
            yield Request(index_x_url,
                          callback=self.parse_fanye,
                          errback=self.error_back,
                          priority=10)

        for y in movie_region:
            index_y_url = 'http://maoyan.com/films' + str(y)
            yield Request(index_y_url,
                          callback=self.parse_fanye,
                          errback=self.error_back,
                          priority=10)

        for z in movie_time:
            index_z_url = 'http://maoyan.com/films' + str(z)
            yield Request(index_z_url,
                          callback=self.parse_fanye,
                          errback=self.error_back,
                          priority=10)

    def parse_fanye(self, response):
        """
        通过请求每一个列表页，拿到每一个详情页的url
        """
        print("进入列表页")
        detail_urls = response.xpath('//div[@class="movies-list"]/dl//dd/div[1]/a/@href').extract()
        print(detail_urls)
        if detail_urls is not None:
            for detail_url in detail_urls:
                # 通过解析回来的url并不完整，需要手动拼接url
                detail_url = 'http://maoyan.com' + str(detail_url)
                print(detail_url)
                yield Request(url=detail_url,
                              callback=self.parse_detail,
                              errback=self.error_back,
                              priority=20)

        print("寻找翻页的url")
        next_url = response.xpath("//li/a[text()='下一页']/@href").extract_first()

        if next_url is not None:
            next_url = 'http://maoyan.com/films' + str(next_url)
            print("下一页的链接:", next_url)
            yield Request(next_url,
                          callback=self.parse_fanye,
                          errback=self.error_back,
                          priority=20)

    def parse_detail(self, response):
        """
        用来解析字段
        """
        html_font = font_creator(response.text)
        # 声明xpath
        resp = Selector(text=html_font)

        # 用xpath定义电影的主要三个大的板块
        brief = resp.xpath('//div[@class="movie-brief-container"]')
        content = resp.xpath('//div[@class="tab-desc tab-content active"]')
        container = "".join(resp.xpath('//div[@class="movie-stats-container"]//text()').extract()).split()

        item = MaoyanscrapyItem()
        # 电影的第一个名字
        item['name_first'] = brief.xpath('h3/text()').extract_first()
        # 电影的第二个名字
        item['name_second'] = brief.xpath('div/text()').extract_first()
        # 电影的链接
        item['url'] = str(response.url)

        # 电影的类型
        item['movie_type'] = brief.xpath('ul/li[1]/text()').extract_first()
        # 电影地区和时间
        item['region_time'] = ''.join(brief.xpath('ul/li[2]/text()').extract()).strip().replace(" ", "").replace("\n", '')
        # 上映时间
        item['release_time'] = brief.xpath('ul/li[3]/text()').extract_first()

        # 已经上映，就有 “用户评价，评价数量，累计票房”字段
        # 没有上映，就有“想看数”字段
        try:
            item['User_ratings'] = container[1]
            item['ratings_num'] = container[2]
            item['piao_fang'] = container[4]
            item['want_look'] = "None"
        except:
            item['User_ratings'] = "None"
            item['ratings_num'] = "None"
            item['piao_fang'] = "None"
            item['want_look'] = container[1]

        # 剧情介绍
        item['plot_introduction'] = "".join(content.xpath('div[1]//text()').extract()).replace("\n", '').replace(" ", "")[4:]
        # 主要演员
        item['actor'] = "".join(content.xpath('div[2]//text()').extract()).split()
        # 如果作品得奖，就有奖项字样，并且存在于class="movie-stats-container"的第3个div下，评论在第5个div下
        # 如果没有作品得奖信息，评论存在于class="movie-stats-container"的第4个div下
        if content.xpath('div[3]/div/h3/text()').extract_first() == "奖项":
            item['awards'] = "".join(content.xpath('div[3]//li//text()').extract()).strip()
            item['awards'] = re.sub('\s{2,}', ',', item['awards'])
            # 如果有奖项评论，提取
            item['comment'] = ''.join([text + "\n\n\n" for text in content.xpath('div[5]//div[@class="comment-content"]/text()').extract()])
        else:
            item['awards'] = "None"
            item['comment'] = ''.join([text + "\n\n\n" for text in content.xpath('div[4]//div[@class="comment-content"]/text()').extract()])

        print(item)
        yield item

    def error_back(self, e):
        """
        报错机制
        """
        self.logger.error(format_exc())
