# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    print(req.text)
    html = req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',class_ = '')
    print(texts)