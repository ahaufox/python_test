# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page=1'

f='UM_distinctid=15d649220579b6-0633085fade7e-36624308-100200-15d649220588b3;Hm_lvt_56df696d8a958fb742e6f8f00d45558a=1503662587,1503665147,1503712226;Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1504589816,1505700253,1506324637;PHPSESSID=r7ptfnpbdu28ashkqp3pt37385'
cookies={}
for line in f.split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value
date=requests.get(url,cookies=cookies)
date=date.text
soup = BeautifulSoup(date,"html.parser")
#获取所有内容

cla=soup.select("body > div.page > ul > span")[0].text
cla=cla.encode('utf-8')
total_number=int(cla[6:-3])
num=(total_number)+9
#保证下面取的时候能取到所有的页
#print '页数：'+str(num/10)
#print '--------------------------------------------------------------------------'
#获取总条数结束
num_yu=total_number%10
#num=3
x=1
#print '总条数：'+str(num)
#print '--------------------------------------------------------------------'
for x in range(142,int(num/10)+1):
    url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page='+str(x)
    f = 'UM_distinctid=15d649220579b6-0633085fade7e-36624308-100200-15d649220588b3;Hm_lvt_56df696d8a958fb742e6f8f00d45558a=1503662587,1503665147,1503712226;Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1504589816,1505700253,1506324637;PHPSESSID=r7ptfnpbdu28ashkqp3pt37385'
    cookies = {}
    for line in f.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    date = requests.get(url, cookies=cookies)
    date = date.text
    soup = BeautifulSoup(date, "html.parser")
    if x<int(num/10):
        i = 0
        for i in range(0, 10):
            tr = soup.select('td')[i * 16].text
            print (tr)
            tr = soup.select('td')[i * 16 + 2].text
            print (tr)
            print '--------------------------------------------------------------------'
    else:
        j = 0
        for j in range(0, num_yu):
            tr = soup.select('td')[j * 16].text
            print (tr)
            tr = soup.select('td')[j * 16 + 2].text
            print (tr)
            print '----------------222222222---------------------------------'
            # 获取所有条目，共10条

