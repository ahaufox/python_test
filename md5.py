# -*- coding:utf-8 -*-
import hashlib
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

m = hashlib.md5()
s="sdfasfd"
s=s.encode("utf8")
m.update(s)
ss=m.hexdigest()
print ss