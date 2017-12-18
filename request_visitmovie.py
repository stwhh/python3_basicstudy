# -*-coding:utf-8-*-
import re

import requests


# 访问电影请求
def request_movie(url):
    ips_all = read_proxyips()
    for index, ip in enumerate(ips_all):  # 列表加了enumerate 可以访问索引
        for key, value in ip.items():
            proxies = {  # 代理类型+地址
                key: value
            }
            # 需要手机抓包看下请求头有哪些东西，现在就写下面俩个
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko)'
                              'Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043520 Safari/537.36 MicroMessenger/6.5.16.1120'
                              'NetType/WIFI Language/zh_CN',
                'Referer': url
            }
            r = requests.get(url, headers=headers, proxies=proxies)
            print('本次运行代理共{} 个，正在进行第{}个代理访问，代理ip为：{}。'.format(len(ips_all), index + 1,value))
            print(r.content.decode('utf-8'))

    print('运行结束')


# 读取代理ip
def read_proxyips():
    with open('D:\\ips.txt', 'r', errors='啊，出错了。') as f:
        ips = []
        while True:
            http_address = f.readline().strip()
            # print(f.read()) # 返回字符串，读取所有
            # print(f.readlines()) # 返回一个列表，每行数据是列表的一个值，可以用for i in list
            if (http_address == ''):
                break
            try:
                pattern = re.compile(r'https?')
                type = re.findall(pattern, http_address)[0]
                address = http_address[len(type) + 1:]
                # print('类型：'+type[0])
                # print('地址：'+address) # 因为http后面有一个空格，所以要+1
                # if(not is_existip(ips,address)): # 验证是否重复，去掉重复的
                ips.append({type: address})
            except BaseException as e:
                print("出错："+e)
                continue

    return ips


# 判断当前ip是否存在列表中
def is_existip(iplist, ip):
    for i in iplist:
        for key, value in i.items():
            if (value == ip):
                return True
    return False


# request_movie('http://fl.108.minghu-rolwal.com/?m=vod-detail-id-18089.html')
request_movie('https://www.baidu.com/')
