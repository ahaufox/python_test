# -*- coding: GBK -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import pymysql.cursors
import threading
# 获取tel的函数
def get_tel(postData):
    url = 'http://51mmt.com/mob/Member/RPC'
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
    s = res_json['content'][0]['key']
    return s
# 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

def insert_tel():
    for n in range(500, 600):
        wr = 5 * n
        sql_userid = 'select id from mmt_list WHERE tel IS NULL limit 0,{}'.format(wr)
        cur.execute(sql_userid)
        ret = cur.fetchall()
        conn.commit()
        list = []
        for i in range(0, wr - 1):
            list.append(ret[i]['id'])
        # id组装
        for ss in list:
            postData = {
                'action': 'callCredits',
                'content[0][type]': '苗店',
                'content[0][userID]': '{}'.format(ss),
                'content[0][callCount]': '2'
            };
            #  获取tel
            print ss
            tel = get_tel(postData)
            # tel写入数据库
            if tel == '':
                sql_user_tel = 'update mmt_list set tel={} WHERE id={}'.format(0, ss)
                cur.execute(sql_user_tel)
                conn.commit()
            else:
                sql_user_tel = 'update mmt_list set tel={} WHERE id={}'.format(tel, ss)
                cur.execute(sql_user_tel)
                conn.commit()


for i in xrange(1000):
    t=threading.Thread(target=insert_tel())
    t.start()
cur.close()
