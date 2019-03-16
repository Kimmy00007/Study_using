#coding=utf-8
from __future__ import unicode_literals
import json
import hashlib
import base64
from base64 import b64encode, b64decode
from url_chuli import Urlchuli
import random
def md_jtpy():
    m = hashlib.md5()
    ordernumber = ''.join(random.sample('1234567890abcdefg',15))
    dict ={"amount":"100","bankAccountName":"熊峰","bankAccountNo":"6236682660004282455","bankCode":"CCB","callBackUrl":"http://127.0.0.1/","charset":"UTF-8","merNo":"JTZF800003","orderNum":ordernumber,"version":"V3.1.0.0"}
    signKey = ('24A7CB47EF50AB94BEBF0859EBC9F23B')
    parmars = json.dumps(dict,separators=(',',':'),ensure_ascii=False) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    dict["sign"]=parmars_md5
    d = dict
    msg = json.dumps(d)
    return msg





