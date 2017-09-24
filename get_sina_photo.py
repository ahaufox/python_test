# coding=utf-8
import requests
import demjson
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
date_url=requests.get('http://api.slide.news.sina.com.cn/interface/api_album.php?activity_size=198_132&size=img&ch_id=3&sub_ch=news&page=3&num=16&jsoncallback=slideNewsSinaComCnCB&_=1506171573969')
date=date_url.text[21:-1]
x=demjson.decode(date)
data=x["data"]
i=0
while i<15:
    url=str(data[i]["img_url"])
    name=str(data[i]["name"])
    name=str(name)
    print (name)
    print (url)
    print("-----------------------------------------------------")
    i+=1