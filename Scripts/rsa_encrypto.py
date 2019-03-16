# -*- coding: utf-8 -*-

import hashlib, base64
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5


# 返回远程文件的大写MD5值
def remote_file_md5(url):
    remote_file = buffer(urllib2.urlopen(url).read())
    m = hashlib.md5()
    m.update(remote_file)
    return m.hexdigest().upper()


# 秘钥对的生成
def rsa_key_gen(hash_digest):
    random_generator = Random.new().read
    rsa_key = RSA.generate(1024, random_generator)   # This will take a while...
    private_pem = rsa_key.exportKey()
    public_pem = rsa_key.publickey().exportKey()

    # 写入文件
    with open('master-private.pem', 'w') as f:
        f.write(private_pem)
    with open('master-public.pem', 'w') as f:
        f.write(public_pem)
    return


# 使用接收方提供的公钥加密
def rsa_encrypt(message):
    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(message))
        return cipher_text


# 使用私钥解密
def rsa_decrypt(encrypt_text):
    with open('master-private.pem') as f:
        random_generator = Random.new().read
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)
        return text


# 使用私钥签名
def rsa_sign(message):
    with open('master-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(message)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
        return signature


# 使用公钥验签
def rsa_verify(message, signature):
    with open('master-public.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(message)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
        return is_verify