# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import urllib2
import json
import pymysql.cursors
import threading
import time
# 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
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
    dict =[]
    dict.append(res_json['content'][0]['storeinfo']['areaName'].strip('\"').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['companyname'].strip('\"').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['address'].encode('UTF-8').strip('\"'))
    dict.append(res_json['content'][0]['storeinfo']['name'].strip('\\').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['jobpostion'].strip('\"').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['introduction'].strip('\"').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['wx'].strip('\"').encode('UTF-8'))
    dict.append(res_json['content'][0]['storeinfo']['goldVIP'])
    dict.append(res_json['content'][0]['storeinfo']['jewelVIP'])
    return dict

#查询已有数据中id最大值
def cat_id_big():
    sql = "select id from mmt_all_info order by id DESC limit 1"
    cur.execute(sql)
    ret = cur.fetchall()
    num = ret[0]
    conn.commit()
    return num['id']
#获取id 的函数
def catch_id(start,write_num):
    list = []
    sql_userid = 'select id from mmt_list where id>{} order by id limit {}'.format(start,write_num)
    cur.execute(sql_userid)
    ret = cur.fetchall()
    conn.commit()
    for n in xrange(write_num):
        list.append(ret[n]['id'])
    return list

#写入数据

def insert_tel_info(write_num):
    sql_f = """insert into mmt_all_info VALUES ("""
    tel_info_id_list = catch_id(cat_id_big(), write_num)  # 获取id的list
    sql = ''
    sql_value={}
    for i in xrange(write_num):
        for tel_info_id in tel_info_id_list:
            postdata_tel = {
                'action': 'callCredits',
                'content[0][type]': '苗店',
                'content[0][userID]': '{}'.format(tel_info_id),
                'content[0][callCount]': '2'
            };
            postdata_info = {
                'action': 'storegetinfo',
                'content[0][id]': '{}'.format(tel_info_id)
            };

            tel = get_tel(postdata_tel)
            if tel == '':
                tel = 0
            else:
                tel = get_tel(postdata_tel)
            info = get_info(postdata_info)

            info.append(tel)
            info.append(tel_info_id)
            sql_value[i] = info
    return sql_value

print  insert_tel_info(2)
cur.close()
