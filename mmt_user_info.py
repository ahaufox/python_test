# -*- coding: utf-8-*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import pymysql.cursors
def get_info(postData):
    url = 'http://51mmt.com/mob/Store/RPC'
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
    dict={}
    dict['areaName'] = res_json['content'][0]['storeinfo']['areaName'].strip('\"').encode('UTF-8')
    dict['companyname'] = res_json['content'][0]['storeinfo']['companyname'].strip('\"').encode('UTF-8')
    dict['address'] = res_json['content'][0]['storeinfo']['address'].encode('UTF-8').strip('\"')
    dict['name'] = res_json['content'][0]['storeinfo']['name'].strip('\\').encode('UTF-8')
    dict['jobpostion'] = res_json['content'][0]['storeinfo']['jobpostion'].strip('\"').encode('UTF-8')
    dict['introduction'] = res_json['content'][0]['storeinfo']['introduction'].strip('\"').encode('UTF-8')
    dict['wx'] = res_json['content'][0]['storeinfo']['wx'].strip('\"').encode('UTF-8')
    dict['goldVIP'] = res_json['content'][0]['storeinfo']['goldVIP']
    dict['jewelVIP'] = res_json['content'][0]['storeinfo']['jewelVIP']
    return dict

# 连接数据库

conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                        user='root',
                        password='root',
                        db='tel',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
# 获取用户id
# 设定一次写入条数
for n in range(500,1000):
    wr = 5 * n
    sql_user_id = 'select id from mmt_list where gold_vip IS NULL limit 0,{}'.format(wr)
    cur.execute(sql_user_id)
    ret = cur.fetchall()
    conn.commit()
    list = []
    for i in range(0, wr - 1):
        list.append(ret[i]['id'])
    # id组装
    xxx=0
    for ss in list:
        postData = {
            'action': 'storegetinfo',
            'content[0][id]': '{}'.format(ss)
        };
        #  获取tel
        xxx=xxx+1
        print '共{}条，第{}条。'.format(wr,xxx)
        info = get_info(postData)
        # tel写入数据库
        sql_user_info = """update mmt_list set area=\"{}\", company_name=\"{}\", address=\"{}\", user_name=\"{}\", job_postion=\"{}\", introduction=\"{}\",wechat=\"{}\",gold_vip=\"{}\",jewel_vip={} WHERE id={}""".format(
            info['areaName'], info['companyname'], info['address'], info['name'], info['jobpostion'],
            info['introduction'], info['wx'], info['goldVIP'], info['jewelVIP'], ss)
        try:
            cur.execute(sql_user_info)
        except:
            continue
        conn.commit()
cur.close()
# 获取数据


