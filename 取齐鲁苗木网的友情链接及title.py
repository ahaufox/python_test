import requests
from bs4 import BeautifulSoup
import sys
import urllib2
reload(sys)
sys.setdefaultencoding('UTF-8')
url='http://www.qlmm.cn/'
date=requests.get(url)
date=date.text
soup = BeautifulSoup(date,"html.parser")
num=len(soup.select('div.ch_link > table > tr > td > a'))

for i in range(1,num):
    href=soup.select('div.ch_link > table > tr > td > a')[i].get('href')
    try:
        date2 = urllib2.urlopen(href)
    except:
        continue
    soup2 = BeautifulSoup(date2, "html.parser")
    title=soup2.select('title')[0].text
    print i, ("\t"), href, ("\t"), title