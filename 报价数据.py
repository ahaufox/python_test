# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://miaobang.huinongtx.com/admin/neworder/new_offer'
f = 'PHPSESSID=7a7dvaa3eihsu195aseoq4pi55'
# 设置cookies
cookies = {}
for line in f.split(';'):
    name, value = line.strip().split('=', 1)
    cookies[name] = value
date = requests.get(url, cookies=cookies)
# 设置cookies结束
date=date.text
soup = BeautifulSoup(date,"html.parser")
cat = soup.select('body > div.page > ul > span')[0].get_text()
#函数提取数字
def OnlyCharNum(s,oth=''):
    s2 = s.lower();
    #fomart = 'abcdefghijklmnopqrstuvwxyz0123456789'
    fomart = '0123456789'
    for c in s2:
        if not c in fomart:
            s = s.replace(c,'');
    return s;
cat=int(OnlyCharNum(cat))+1

#获取所有内容
for x in range(1,3):
    url = 'http://miaobang.huinongtx.com/admin/neworder/new_offer?page='+str(x)
    date = requests.get(url, cookies=cookies)
    date=date.text
    soup = BeautifulSoup(date,"html.parser")
#获取所有内容结束
    for i in range(1,16):
        f = open('xx.txt', 'a')
        name=soup.select('td')[i*7-6].get_text()
        name.encode('gbk')
        uptime = soup.select('td')[i * 7 - 2].get_text()
        f.write(name.encode('utf-8'))
        f.write('    ')
        f.write(uptime)
        f.write('\n')
        f.close()
