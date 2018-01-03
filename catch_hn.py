# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
#地址与post的字段
html='http://devwap.huinongtx.com/_api/index.php?api=/supdemand/Purchaselist_Purchaselist.Getpurchaselist'
values = {'start' : '0',
          'limit' : '1',
          'one_id' : '' ,
          'two_id':'',
          'provinceid':'0',
          'cityid':'0',
          'areaid':'0'}
#拼接
data = urllib.urlencode(values)
request = urllib2.Request(html,data)
response = urllib2.urlopen(request)
the_page = response.read()
#请求结束

#获取指定数据
soup=BeautifulSoup(the_page, "html.parser")
tel=soup.select('key')[0].text
print (tel)
print  the_page
