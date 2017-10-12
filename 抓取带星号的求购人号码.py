# -*- coding:gb2312 -*-
import requests
import time
from bs4 import BeautifulSoup
for i in range(1,8):
    url='http://www.huamu.com/index.php?app=requirement&act=index&cate_id=0&region_id=0&keyword_sr=&order=add~time%20desc&page='+str(i)
    date=requests.get(url)
    date=date.text
    soup = BeautifulSoup(date,"html.parser")
    for i in range(0,21):
        cla=soup.select("body > div.content > div.c2_right_view.gleft > div.squares > table > tbody > tr > td > a")[i*2-1]
        cla=cla.text
        print cla
    time.sleep(1)