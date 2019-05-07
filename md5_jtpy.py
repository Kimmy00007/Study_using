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
    dict ={}
    signKey = ''
    parmars = json.dumps(dict,separators=(',',':')) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    dict["sign"]=parmars_md5
    d = dict
    msg = json.dumps(d)
    return msg


