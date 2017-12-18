# -*-coding:utf-8-*-
import random
import re
import time
import requests


# 刷访问量程序
class AddVisit:
    def __init__(self, url, is_use_proxy):
        '''
        :param url: 要访问的地址
        :param is_use_proxy: 是否用代理
        '''
        self.url = url
        self.is_use_proxy = is_use_proxy

    # 访问地址
    def get_request(self):
        url = self.url
        ips_all = self.read_proxyips()
        for index, http_address in enumerate(ips_all):  # 列表加了enumerate 可以访问索引
            # print(http_address)
            http_type = http_address['http_type']
            ip = http_address['ip']
            try:
                proxies = {  # 代理类型+地址
                    http_type: ip
                }
                # 需要手机抓包看下请求头有哪些东西，现在就写下面俩个
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043520 Safari/537.36 MicroMessenger/6.5.16.1120 NetType/WIFI Language/zh_CN',
                    'Referer': url
                }
                if (self.is_use_proxy):
                    r = requests.get(url, headers=headers, proxies=proxies, timeout=3)
                    print('【时间 {}】本次运行代理共{} 个，正在进行第{}个代理访问，代理ip为：{}。'
                          .format(time.time(), len(ips_all), index + 1, ip))
                    print('【运行结果】：{0}\n'.format(r.status_code))
                    # print(r.content.decode('utf-8'))
                    print(r.text)
                else:
                    r = requests.get(url, headers=headers)
                    print('【时间 {}】本次运行并未使用代理'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    print('【运行结果】：{0}\n'.format(r.status_code))
                    # print(r.content.decode('utf-8'))
                    print(r.text)
            except BaseException as ex:
                print("【时间 {}】请求出错，IP：{}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), ip))
                print("异常如下：{}\n".format(ex))
                continue
        time.sleep(random.randint(3, 6))  # 爬完一个相册之后等待3-6秒再爬，防止反爬虫

        print('运行结束')

    # 读取代理ip
    def read_proxyips(self):
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
                    ip = http_address[len(type) + 1:]  # 因为http后面有一个空格，所以要+1 截取ip
                    # print('类型：'+type[0])
                    # print('地址：'+ip)
                    # if(not self.is_existip(ips,ip)): # 验证是否重复，去掉重复的
                    ips.append({'http_type': type, 'ip': ip})
                except BaseException as e:
                    print("出错：" + e)
                    continue

        return ips

    # 判断当前ip是否存在列表中
    def is_existip(self, iplist, ip):
        '''
        判断当前ip是否存在列表中
        :param ip: 当前需要判断的ip
        :return: true:存在 false:不存在
        '''
        for i in iplist:
            for key, value in i.items():
                if (value == ip):
                    return True
        return False


# AddVisit('https://www.cnblogs.com/', True).get_request()
AddVisit('http://fl.108.minghu-rolwal.com/?m=vod-detail-id-18089.html', False).get_request()
