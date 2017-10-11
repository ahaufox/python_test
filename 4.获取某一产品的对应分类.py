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
cookies={'PHPSESSID': '7a7dvaa3eihsu195aseoq4pi55'}
date=requests.get(url,cookies=cookies).text
soup = BeautifulSoup(date,"html.parser")
cat=soup.div.p.text
cat=cat.encode('gbk')
#cat里面是json数据
f=open('cat.json','wb')
f.write(cat)
f.close()
#cat存入json文件
f = open("cat.json")
setting = json.load(f)
oneId = setting['oneId']
twoId= setting['twoId']
threeId= setting['threeId']
fourId=setting['fourId']

print (oneId)
print (twoId)
print (threeId)
print (fourId)
