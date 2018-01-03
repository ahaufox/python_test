# -*- coding:utf-8 -*-
import sys
import pymysql.cursors


conn = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='root',
                           db='tel',
                           charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)

cur = conn.cursor()
sql="select * from tel_md5"
#" where md5_tel=\"\""
cur.execute(sql)
ret = cur.fetchall()
conn.commit()

#关闭连接对象
def md5(str):
    import hashlib
    m = hashlib.md5()
    str = str.encode("utf8")
    m.update(str)
    return m.hexdigest()

for i in range(50000,60000):
    cur = conn.cursor()
    cur.execute("update tel_md5 set md5_tel=\"{}\" where tel = {}".format(md5(ret[i]["tel"]),ret[i]["tel"]))
    conn.commit()
    print(ret[i]["id"])

cur.close()