#coding=utf-8
import json
import hashlib
import base64
from base64 import b64encode, b64decode
from url_chuli import Urlchuli
import random
def md_jtpy():
    m = hashlib.md5()
    ordernumber = ''.join(random.sample('1234567890abcdefg',15))
    dict ={"amount":"100","callBackUrl":"http://127.0.0.1/","callBackViewUrl":"http://www.baidu.com/","charset":"UTF-8","goodsName":"book","merNo":"JTZF800003","netway":"E_BANK_CCB","orderNum":ordernumber,"random":"KJ12","version":"V3.1.0.0"}
    signKey = ('24A7CB47EF50AB94BEBF0859EBC9F23B')
    parmars = json.dumps(dict,separators=(',',':')) + signKey
    b = parmars.encode('utf-8')
    m.update(b)
    parmars_md5= m.hexdigest().upper()
    dict["sign"]=parmars_md5
    d = dict
    msg = json.dumps(d)
    return msg



