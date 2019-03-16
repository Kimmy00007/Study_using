#coding=utf-8
import re
import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import requests
from base64 import b64encode, b64decode
import rsa
from urllib.parse import quote
from md5_jtpy1 import md_jtpy

def rsa_encrypt(msg,pubkey):
    pub_title = pubkey
    pubkey_str ='-----BEGIN PUBLIC KEY-----' + '\n' + pub_title + '\n' + '-----END PUBLIC KEY-----'
    msg = md_jtpy().encode(encoding="utf-8")
    length = len(msg)
    default_length = 117
    #公钥加密
    pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(pubkey_str))
    # 长度不用分段
    if length < default_length:
        encry_text = base64.b64encode(pubobj.encrypt(msg))
        encry_value = encry_text.decode('utf-8')
        return encry_value
    #需要分段
    offset = 0
    res = b''
    while length - offset > 0:
        if length - offset > default_length:
            res += (pubobj.encrypt(msg[offset:offset + default_length]))
        else:
            res += (pubobj.encrypt(msg[offset:]))
        offset += default_length
    return base64.b64encode(res).decode('utf-8')

if __name__ == '__main__':
    pubkey='MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmqMcfRtBl6sBmh2rLD' \
           '9DjaALlhrIIWiSVOA79hRUMJj9mYg5sjNeTjsEfutv294luUTA2dyzOdB' \
           '6gV+RNRkso8W8h+GcvNoPUee3JKI2aryFOlvjtoKAvKN7RDRXcICfFB+K' \
           'EZNaAX8KRETc5Lr0L3t8SIi//JeSssJoq7FgiDwIDAQAB'
    for i in range(30):
        msg = md_jtpy()
        request_url = 'http://api-test.jiutongpay.com.cn/api/remit.action'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        a = rsa_encrypt(msg,pubkey)
        b = quote(a,'utf-8')
        request_data = "data="+b+"&merchNo=JTZF800003&version=V3.1.0.0"
        c = "".join(request_data)
        #c = c.encode("utf-8")
        head = {"Content-Type": "application/x-www-form-urlencoded"}
        print ('客户端请求JSON报文数据为（客户端 --> 服务端）:\n', c)
        # 客户端发送请求报文到服务端

        # r = requests.get(request_url + "?" + c, "")
        r = requests.post(request_url, data=request_data, headers=head)
        # 客户端获取服务端的响应报文数据
        responsedata = r.text
        print ('服务端的响应报文为（客户端 <--服务端）: ', responsedata)
        print ("get the status: ", r.status_code)