# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import pymysql.cursors
import urllib2
from bs4 import BeautifulSoup
reload(sys)
connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='root',
                             db='HtmlToTitle',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)
cur = connection.cursor()
sql="select * from html_title where title is NULL"
#" where md5_tel=\"\""
cur.execute(sql)
connection.commit()
ret = cur.fetchall()
num=100
for i in range(0,num):
    print ret[i]['id']
    h=ret[i]['html'].encode('utf-8')
    href=('http://{}'.format(h))
    date2 = urllib2.urlopen(href, timeout=5)
    soup = BeautifulSoup(date2, "html.parser")
    title=soup.select('title')[0].text
    sql =("update html_title set title=\"{}\" where id={}".format(title.encode('utf-8'),ret[i]['id']))
    cur.execute(sql)
    print  ret[i]['id']
cur.close()