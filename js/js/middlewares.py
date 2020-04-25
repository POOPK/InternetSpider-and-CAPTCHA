# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http.response.html import HtmlResponse #准备返回一个封装过的response
import time


class JsSpiderMiddleware(object):
    def __init__(self):
        self.wb = webdriver.Chrome('E://chromedriver.exe') #位置不一定

    def process_request(self,request,spider):
        self.wb.get(request.url)
        time.sleep(1)
        try:
            while True:
                showmore = self.wb.find_element_by_xpath('//*[@id="__next"]/div[1]/div/div[1]/section[3]/div[1]/div')
                showmore.click()
                time.sleep(0.3)
                if not showmore:
                    break
        except:
            pass
        response = HtmlResponse(url=self.wb.current_url,body=self.wb.page_source,request=request,encoding='utf-8')#.page_source是该网页的源代码 current_url是当前网页的url



        return response
