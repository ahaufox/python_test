# -*- coding: utf-8-*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import random
import pymysql.cursors
import time

url='http://51mmt.com/mob/Contact/RPC?xx='+str(random.random())

def get_list(postData):
    conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

    cur = conn.cursor()
    data = urllib.urlencode(postData)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255',
        'Cookie': 'ASP.NET_SessionId=cchnw3ke0k3ktbqzhrzfu2g4'}
    request = urllib2.Request(url, data, headers=headers)
    response = urllib2.urlopen(request)
    # 获取指定数据
    soup = BeautifulSoup(response, "html.parser")
    res = soup.text
    res_json = json.loads(res)
    x = len(res_json['content'])
    for i in range(0, x):
        s = res_json['content'][i]['id']
        sql = "insert into mmt_list(id) values ({})".format(s)
        cur.execute(sql)
        conn.commit()
    cur.close()

for i in  range(1,3):
    postData = {
        'action': 'quanbooklist',
        'content[0][qid]': '10',
        'content[0][pageindex]': '{}'.format(i),
        'content[0][pagesize]': '200',
    };
    get_list(postData)
    w=random.randint(0,20)
    w2=w/100
    time.sleep(w2)
    print '第{}页采集完成'.format(i)


