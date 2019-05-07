from md5_jtpy import md_jtpy
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
from urllib.parse import quote
import json
import hashlib

def rsa_decrypt(biz_content,prikey):
    biz_content = base64.b64decode(biz_content.encode())
    len_content = len(biz_content)
    default_length = 128
    #私钥解密
    priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(prikey))
    #长度不用分段
    if len_content < default_length:
        return b''.join(priobj.decrypt(biz_content,b'failure'))
    offset = 0
    params_lst = []
    while len_content - offset > 0:
        if len_content - offset > default_length:
            params_lst.append(priobj.decrypt(biz_content[offset:offset+default_length],b'failure'))
        else:
            params_lst.append(priobj.decrypt(biz_content[offset:],b'failure'))
        offset += default_length
    target = b''.join(params_lst)
    return target

if __name__ == '__main__':
    with open('rsa-public.pem','r',encoding = 'utf-8') as f:
        pubkey = f.read()
    with open('rsa-private.pem','r',encoding = 'utf-8') as g:
        prikey = g.read()
    biz_content = "dPKo8p37Jl4O+sKemAYqa9liJI5NUFHuEs0D71xnxa0OavXOEgB7X+B7wzQZVJ6ZBmJ7Xp" \
                  "NIpPhA2mghowRxVX2vgZ03VykpqOz8XJQlROYhIru+isJKGYj/K2qwlxdIhklYLr0XMoP8" \
                  "cPA2nlqIJ9FiwCHfLMPU5u/ro8LEPq4OjAfZcNftAV9uSR4G5ZzWfpvxP3tIh9ecIe3pyH" \
                  "caDmuWxPfFc3bDkR4jEVx8ZbPtXuCM6iiCdaHaKgGlcAyMa8cIxzPIcvPytV8hQq+rkf3E" \
                  "iP+dmZsXedtxsB/D1Dlnz5/F/eKpExE6UyaGAcsKSDgY6pYBLTXesxKasKE5Fg=="
    decrypt_pay = rsa_decrypt(biz_content,prikey)
    print("异步通知报文：",decrypt_pay)
    decrypt_pay = str(decrypt_pay, encoding="utf-8")
    data = eval(decrypt_pay)
    data.pop('sign')
    parmars = json.dumps(data, separators=(',', ':'))
    print("移除sign：",parmars)
    signKey = "810479A90CB5231C908603BC7E8C0D6A"
    a = (parmars + signKey).encode('utf-8')
    m = hashlib.md5()
    m.update(a)
    parmars_md5 = m.hexdigest().upper()
    print("验签结果：",parmars_md5)

