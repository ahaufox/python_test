# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

for x in range(12,14):
    url = 'http://miaobang.huinongtx.com/admin/neworder/new_offer?page='+str(x)
    f='Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1500133174; Hm_lpvt_f4eb02735f3a928a83977ee219444a3e=1500133174; PHPSESSID=su274ghuuiafam2ujt5phgtoj4'
    cookies={}
    for line in f.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    date=requests.get(url,cookies=cookies)
    date=date.text
    soup = BeautifulSoup(date,"html.parser")
#获取所有内容
    for i in range(1,16):
        f = open('xx.txt', 'a')
        name=soup.select('td')[i*7-6].get_text()
        name_before = name = soup.select('td')[(i - 1) * 7 - 6].get_text()
        name.encode('gbk')
        uptime = soup.select('td')[i * 7 - 2].get_text()
        uptime_before = soup.select('td')[(i-1) * 7 - 2].get_text()
        if i>1:
            if name==name_before and uptime==uptime_before:


        f.write(name.encode('utf-8'))
        f.write('    ')
        f.write(uptime)
        f.write('\n')
        f.close()