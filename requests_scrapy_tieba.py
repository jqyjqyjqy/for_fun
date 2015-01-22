#!/usr/bin/python
# -*- coding:utf-8 -*-
#---------------------------------------  
#   程序：百度贴吧直播贴爬虫 -- scrapy+xpath版本
#   版本：1.0
#   作者：jq  
#   日期：2015.1.20
#   语言：Python 2.7  
#   操作：./tieba.py 帖子网址 | python tieba.py 帖子网址
#   功能：实时输出最新的直播内容
#---------------------------------------  
import requests
from scrapy.selector import HtmlXPathSelector
from scrapy import Selector
import sys, time
BeforeContents = []

def get_contents(results):
    hxs = Selector(text = results)
    contents = hxs.xpath('//div[@class="d_post_content_main"]/div[1]/cc[1]/div[1]/text()').extract()
    for content in contents:
        if content in BeforeContents:
            pass
        else:
            BeforeContents.append(content)
            print '*'*50
            print content
            print '*'*50

def get_html(ID, page):
    url = 'http://tieba.baidu.com/p/%s?see_lz=1&pn=%s' % (ID, page)
    res = requests.get(url)
    results = res.text
    return results

def check_next_page(ID, results, next_num):
    hxs = Selector(text = results)
    hrefs = hxs.xpath('//a[@href="/p/%s?see_lz=1&pn=%s"]/@href' % (ID, next_num)).extract()
    if len(hrefs) > 0:
        return True
    return False

def work(ID):
    page = 1
    results = get_html(ID, page)
    get_contents(results)
    while True:
        if check_next_page(ID, results, page+1):
            page += 1
            results = get_html(ID, page)
            get_contents(results)
        else:
            results = get_html(ID, page)
            get_contents(results)
            time.sleep(10)

if __name__ == '__main__':
    file_name = __file__
    len_sys = len (sys.argv)
    if len_sys != 2 and len_sys != 3:
        if file_name[0] == '.':
            print ("Usage: %s url" % sys.argv[0])
        else:
            print ("Usage: python %s url" % sys.argv[0])
        sys.exit(1)
    url = sys.argv[1]
    url = url.split('tieba.baidu.com/p/')
    url = url[1]
    url = url.split('?')
    work(url[0])
