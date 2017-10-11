# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page=1'
cookies={'PHPSESSID': '7a7dvaa3eihsu195aseoq4pi55'}
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
for x in range(1,int(num/10)+1):
    url = 'http://miaobang.huinongtx.com/admin/gq_supply/index?is_sale=0&add_time=&member_name=&is_recommend=0&product_name=&pro_id=&city_id=&country_id=&is_self_define=1&is_audit=2&is_audit=2&page='+str(x)
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
