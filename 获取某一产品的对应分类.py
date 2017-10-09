# -*- coding:gbk -*-
import requests
from bs4 import BeautifulSoup
import json
pc_name="石楠"
one_id="1"
post="/admin/gq_new_product_class/getAjaxClassList"
id=1
type=2
url = 'http://miaobang.huinongtx.com'+post+'?'+'id=997&type=2'

f = 'UM_distinctid=15d649220579b6-0633085fade7e-36624308-100200-15d649220588b3;Hm_lvt_56df696d8a958fb742e6f8f00d45558a=1503662587,1503665147,1503712226;Hm_lvt_f4eb02735f3a928a83977ee219444a3e=1504589816,1505700253,1506324637;PHPSESSID=r7ptfnpbdu28ashkqp3pt37385'
cookies={}
for line in f.split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value
date=requests.get(url,cookies=cookies)
date=date.text
soup = BeautifulSoup(date,"html.parser")
cat=soup.div.p.text
cat=cat.encode('gbk')
#cat里面是json数据
f=open('cat.json','wb')
f.write(cat)
f.close()
#cat存如json文件
f = open("cat.json")
setting = json.load(f)
oneId = setting['oneId']
twoId= setting['twoId']
threeId= setting['threeId']
print (oneId)
print (twoId)
print (threeId)