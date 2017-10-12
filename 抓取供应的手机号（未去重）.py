# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

for x in range(4,200):
    url='http://www.huamu.com/index.php?app=category&cate_id=1&region_id=0&price=0&ev=&pinyin=lvhuamiaomu&order=add~time%20desc&page={}'.format(str(x))
    date=requests.get(url)
    date=date.text
    soup = BeautifulSoup(date,"html.parser")
    for i in range(0,23):
        cla=soup.select('ul.list_pic > li > p > a')[i].get('href')
        #print cla
        date2 = requests.get(cla)
        date2=date2.text
        soup2 = BeautifulSoup(date2, "html.parser")
        if len(soup2.select('b.color_red'))==1:
            tel = soup2.select('b.color_red')[0].text
            tel = tel.encode('utf-8')
            f = open('tel.txt', 'a')
            f.write(tel)
            f.write('\n')
            f.close()
            print ('    ' + str(i))
        else:
            print ('    ')
    print (x)


print ('down')