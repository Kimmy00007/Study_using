#coding=utf-8
import requests

def test():
    url = "http://biz-test.jiutongpay.com.cn"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    s = requests.session()
    r = requests.get(url=url,headers=headers,verify=Flase)
    print(s.cookies)
    c = requests.cookies

if __name__ == "__main__":
    test()