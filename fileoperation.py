# -*-coding:utf-8-*-

import urllib
from urllib import request
from json import loads
import re


def getUrlList():
    html = urllib.request.urlopen(r'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    response=html.read();
    page=response.decode('GBK');
    # print(page)
    # print(type(page))
    # print(loads(page))
    return loads(page)['data']['searchDOList']


    # response = request.urlopen(r'https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')  # <http.client.HTTPResponse object at 0x00000000048BC908> HTTPResponse类型
    # page = response.read()
    # page = page.decode('GBK')
    # print(page)


# print(type(getUrlList()))
for i in getUrlList():
    print(i["realName"])
