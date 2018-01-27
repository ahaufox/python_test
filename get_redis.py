# coding=utf-8
import redis
import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='root',
                       db='catch_tel',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()
pool=redis.ConnectionPool(host='139.196.173.61',port=6379,password='sh9gUINm6uN1t9IR', decode_responses=True,db=12)
r=redis.Redis(connection_pool=pool)

for i in range(44759,44760):
    if r.get('hntx_mc_login:{}:last_login_time'.format(i)) is None:
        sql = 'insert into hntx_mc_login (user_id) values(\'{}\')'.format(i)
    else:
        last_login_time = r.get("hntx_mc_login:{}:last_login_time".format(i))[2:-1].encode('utf-8')
        login_time = r.get("hntx_mc_login:{}:login_time".format(i))[2:-1].encode('utf-8')
        app_version = r.hget("hntx_mc_login:{}:terminal_info".format(i), "app_version").encode('utf-8')
        device_model = r.hget("hntx_mc_login:{}:terminal_info".format(i), "device_model").encode('utf-8')


        if r.hget("hntx_mc_login:{}:terminal_info".format(i), "device_token") is None:
            device_token = r.hget("hntx_mc_login:{}:terminal_info".format(i), "device_token")
        else:
            device_token = r.hget("hntx_mc_login:{}:terminal_info".format(i), "device_token").encode('utf-8')
        system_type = r.hget("hntx_mc_login:{}:terminal_info".format(i), "system_type").encode('utf-8')
        from_tag = r.hget("hntx_mc_login:{}:terminal_info".format(i), "from_tag").encode('utf-8')
        times = r.get("hntx_mc_login:{}:times".format(i)).encode('utf-8')
        sql='insert into hntx_mc_login (user_id,last_login_time,login_time,app_version,device_model,device_token,system_type,times) ' \
        'values(\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\',\'{}\')'.format(i,int(last_login_time),int(login_time),app_version,device_model,system_type,from_tag,int(times))
    cur.execute(sql)
    conn.commit()
    print i
