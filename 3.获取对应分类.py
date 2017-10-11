# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import demjson
pc_name="石楠"
one_id="1"
post="/admin/gq_new_product_class/getAjaxClassList"
id=1
type=2
url = 'http://miaobang.huinongtx.com'+post+'?'+'id=9897&type=2'
cookies={'PHPSESSID': '7a7dvaa3eihsu195aseoq4pi55'}
date=requests.get(url,cookies=cookies)
date=date.text
soup = BeautifulSoup(date,"html.parser")
cat=soup.div.p.text
#cat里面是json数据
#cat=demjson.decode(cat)
print cat