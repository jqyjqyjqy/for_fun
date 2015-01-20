#!/usr/bin/python
#coding=utf-8
#---------------------------------------  
#   程序：百度贴吧直播贴爬虫--正则表达式版本
#   版本：1.2
#   作者：jq  
#   日期：2014.7.3  
#   语言：Python 2.7  
#   操作：./tieba.py 网址 | python tieba.py 网址
#   功能：实时输出最新的直播内容
#---------------------------------------  
import httplib
import os
import re
import sys
import time
All = []

def get_zhibo (results):
    reg = '\<div id="post_content_\d+" class="d_post_content j_d_post_content "\>([\w\W]*?)\</div\>'
    p = re.compile(reg)
    global All
    #url = p.findall (results.decode('gbk'))
    now = p.finditer(results)
    for match2 in now:
        tmp=match2.group(1)
        tmp=re.sub(r'\<br\>','\n',tmp)
        tmp=re.sub(r'\<[\w\W]*?\>','',tmp)
        if tmp in All:
            pass
        else:
            All.append(tmp)
            print '*'*50
            print tmp
            print '*'*50
def get_html(downconn, ID, page):
    url = '/p/%s?see_lz=1&pn=%s' % (ID, page)
    downconn.request ("GET", url)
    down = downconn.getresponse ()
    results = down.read ()
    return results#.decode('gbk')

def hav_next(results, next_num):
    reg = '\<a href="(/p/\d+?\?see_lz=1&pn=\d+?)"\>%s' % next_num
    hav=re.search(reg, results)
    if hav:
        #print 'yes'
        return True
    #print 'no'
    return False
def work(ID):
    downconn = httplib.HTTPConnection ("tieba.baidu.com")
    page = 1
    results = get_html(downconn, ID, page)
    get_zhibo(results)
    while True:
        try:
            if hav_next(results, page+1):
                page += 1
                results = get_html(downconn, ID, page)
                get_zhibo(results)
            else:
                results = get_html(downconn, ID, page)
                get_zhibo(results)
                time.sleep(10)
        except Exception:
            pass

if __name__ == '__main__':
    file_name = __file__
    len_sys = len (sys.argv)
    if len_sys != 2 and sys.argv != 3:
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
