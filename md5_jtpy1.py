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
    Req_ser_par ={"amount":"100","bankAccountName":"熊峰","bankAccountNo":"6236682660004282455","bankCode":"CCB","callBackUrl":"http://c57bc06c.ngrok.io/remitCallback","charset":"UTF-8","merNo":"JTZF800003","orderNum":ordernumber,"version":"V3.1.0.0"}
    signKey = '72977756EF09F52B8A272AEC19A478C6'
    parmars = json.dumps(Req_ser_par,separators=(',',':'),ensure_ascii=False) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    print(parmars_md5)
    Req_ser_par["sign"]=parmars_md5
    msg = json.dumps(Req_ser_par)
    print(msg)
    return msg





