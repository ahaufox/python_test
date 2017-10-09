# -*- coding:utf-8
import requests

username='admin'
password='mbb%402017%25TGBnhy6'
captcha_url='http://miaobang.huinongtx.com/captcha.html'
login_url='http://miaobang.huinongtx.com/admin/index/login.html'
post_url='http://miaobang.huinongtx.com/admin/index/login'+'?'
code=requests.get(captcha_url)
f = open('code.png', 'wb')
f.write(code.content)
f.close()
result=requests.get(post_url+'username='+username+'&password='+password+'&captcha=jjaj').text
print (post_url+'username='+username+'&password='+password+'&captcha=jjaj')