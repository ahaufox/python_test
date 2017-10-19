# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('UTF-8')
for x in range(0,20):
    url='http://www.baidu.com/s?wd={}&pn={}'.format("苗木买卖",x*10)
    date=urllib2.urlopen(url)
    soup=BeautifulSoup(date, "html.parser")
    num=len(soup.select('a.c-showurl'))
    for i in range(0,num):
        soup2 = soup.select('a.c-showurl')[i].text
        soup2.replace('https://', '', 2)
        soup2.replace('http://', '', 2)
        f=open('baidu.txt','a')
        f.write(soup2)
        f.write('\n')
        f.close()
    print (url)