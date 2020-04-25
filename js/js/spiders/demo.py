# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from js.items import JsItem


class DemoSpider(CrawlSpider):
    name = 'demo'
    allowed_domains = ['www.jianshu.com']
    start_urls = ['http://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        print('*'*40)
        title = response.xpath('//h1[@class="_1RuRku"]/text()').extract_first()
        article_id = response.url.split('/')[4]
        content = response.xpath('//*[@id="__next"]/div[1]/div/div/section[1]/article').extract_first()#不要用text() 要保存原格式
        pub_time = response.xpath('//div[@class="s-dsoj"]/time/text()').extract_first()
        word_numbers = response.xpath('//div[@class="s-dsoj"]/span[2]/text()').extract_first()
        read_numbers = response.xpath('//div[@class="s-dsoj"]/span[3]/text()').extract_first()
        print('*'*40)
        print(title, article_id, content,pub_time,word_numbers,read_numbers)
        splite_line = '*'*40
        item = JsItem(title=title,article_id=article_id,content=content,pub_time=pub_time,word_numbers=word_numbers,read_numbers=read_numbers,splite_line=splite_line)
        yield item

