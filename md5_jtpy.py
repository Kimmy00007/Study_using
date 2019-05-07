#coding=utf-8
import json
import hashlib
import base64
from base64 import b64encode, b64decode
import random
import datetime
import time
def md_jtpy():
    m = hashlib.md5()
    order_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    ordernumber = order_time + ''.join(random.sample('1234567890aceg',6))
    dict ={"amount":"210","callBackUrl":"http://d1d6aef7.ngrok.io/payCallback","callBackViewUrl":"http://d1d6aef7.ngrok.io/listPayCallbackData","charset":"UTF-8","goodsName":"fish","merNo":"JTZF800003","netway":"E_BANK_CCB","orderNum":ordernumber,"random":"JU47","version":"V3.1.0.0"}
    signKey = '72977756EF09F52B8A272AEC19A478C6'
    parmars = json.dumps(dict,separators=(',',':')) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    dict["sign"]=parmars_md5
    d = dict
    msg = json.dumps(d)
    return msg


