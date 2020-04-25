# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class JsPipeline(object):
    def open_spider(self,spider):
        print('the spider begined...')

    def process_item(self, item, spider):
        text_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'texts')
        text_name = item['title']+'.txt'
        if not os.path.exists(text_path):
            os.mkdir(text_path)
        with open(os.path.join(text_path,text_name),'w',encoding='utf-8') as f:
            for i in ['title','article_id','author','pub_time','word_numbers','read_numbers','splite_line','content']:
                f.write(item[i]+'\n')

    def close_spider(self,spider):
        print('the spider closed...')
