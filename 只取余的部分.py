# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page=1'

f='UM_distinctid=15d649220579b6-0633085fade7e-36624308-100200-15d649220588b3; Hm_lvt_56df696d8a958fb742e6f8f00d45558a=1503662587,1503665147,1503712226; Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1504589816,1505700253,1506324637; PHPSESSID=o37e6vplqn5j0pkjafjokgjbh1'
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
for x in range(145,146):
    url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page='+str(x)
    f = 'UM_distinctid=15d649220579b6-0633085fade7e-36624308-100200-15d649220588b3; Hm_lvt_56df696d8a958fb742e6f8f00d45558a=1503662587,1503665147,1503712226; Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1504589816,1505700253,1506324637; PHPSESSID=o37e6vplqn5j0pkjafjokgjbh1'
    cookies = {}
    for line in f.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    date = requests.get(url, cookies=cookies)
    date = date.text
    soup = BeautifulSoup(date, "html.parser")

    if x>144:
        j = 0
        for j in range(0, 6):
            tr = soup.select('td')[j * 16].text
            print (tr)
            tr = soup.select('td')[j * 16 + 2].text
            print (tr)
            print '--------------------------------------------------------------------'
            # 获取所有条目，共10条

