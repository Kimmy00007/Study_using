#coding=utf-8
from __future__ import unicode_literals
import json
import hashlib
import base64
from base64 import b64encode, b64decode
import random
import datetime
def  md_jtpy():
    m = hashlib.md5()
    order_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    ordernumber = order_time + ''.join(random.sample('1234567890',9))
    Req_ser_par ={}
    signKey = ''
    parmars = json.dumps(Req_ser_par,separators=(',',':'),ensure_ascii=False) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    print(parmars_md5)
    Req_ser_par["sign"]=parmars_md5
    msg = json.dumps(Req_ser_par)
    print(msg)
    return msg





