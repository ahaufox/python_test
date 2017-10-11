# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
pc_name="石楠"
one_id="1"
url = 'http://miaobang.huinongtx.com/admin/gq_new_product_class/detectClassName?pc_name='+pc_name+'&one_id='+one_id
cookies={'PHPSESSID': '7a7dvaa3eihsu195aseoq4pi55'}
date=requests.get(url,cookies=cookies)
date=date.text
soup = BeautifulSoup(date,"html.parser")
cat=soup.div.p.text
print (soup)