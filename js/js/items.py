# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JsItem(scrapy.Item):
    title = scrapy.Field()
    article_id = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    pub_time = scrapy.Field()
    word_numbers = scrapy.Field()
    read_numbers = scrapy.Field()
    splite_line = scrapy.Field()
    pass
