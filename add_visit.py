# -*-coding:utf-8-*-
import random
import re
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys


# 刷访问量程序
class AddVisit:
    def __init__(self, url, is_use_proxy):
        '''
        :param url: 要访问的地址
        :param is_use_proxy: 是否用代理
        '''
        self.url = url
        self.is_use_proxy = is_use_proxy

    # 访问电影网站地址【非模拟，应该可以用，缺少大量代理ip测试】
    def get_request_movie(self):
        url = self.url
        ips_all = self.read_proxyips()
        success_count = 0;
        fail_count = 0;
        for index, http_address in enumerate(ips_all):  # 列表加了enumerate 可以访问索引
            # print(http_address)
            http_type = http_address['http_type']
            ip = http_address['ip']
            try:
                proxies = {  # 代理类型+地址
                    http_type: ip
                }

                # 电影
                headers = {
                    'Host': 'fl.108.minghu - rolwal.com',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,en-US;q=0.8'
                }

                if (self.is_use_proxy):
                    print('【时间 {}】本次运行代理共{} 个，正在进行第{}个代理访问，代理ip为：{}。'
                          .format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), len(ips_all), index + 1, ip))
                    r = requests.get(url, headers=headers, proxies=proxies, timeout=8)
                    print('【运行结果】：{}\n'.format(r.status_code))
                    if r.status_code == 200:
                        success_count += 1
                        # print(r.content.decode('utf-8'))
                        # print(r.text)
                else:
                    r = requests.get(url, headers=headers)
                    print('【时间 {}】本次运行并未使用代理'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    print('【运行结果】：{0}\n'.format(r.status_code))
                    if r.status_code == 200:
                        success_count += 1
                        # print(r.content.decode('utf-8'))
                        # print(r.text)
            except BaseException as ex:
                print("【运行结果】=> 出错：{0}\n".format(ex))
                fail_count += 1
                continue
        time.sleep(random.randint(0, 1))  # 爬完一个相册之后等待2-5秒再爬，防止反爬虫

        print('运行结束,本次运行代理总数：{}，成功数量为：{}，失败数量为：{}'.format(len(ips_all), success_count, fail_count))

    # 访问文章【非模拟，一般不适用访问文章类的，因为有时间限制】
    def get_request_article(self, platform_type):
        '''
        访问文章请求
        :param platform_type: 1：口袋看点 必须打开更多，阅读3秒以上
        :return:
        '''
        url = self.url
        ips_all = self.read_proxyips()
        success_count = 0;
        fail_count = 0;
        for index, http_address in enumerate(ips_all):  # 列表加了enumerate 可以访问索引
            # print(http_address)
            http_type = http_address['http_type']
            ip = http_address['ip']
            try:
                proxies = {  # 代理类型+地址
                    http_type: ip
                }
                if (platform_type == 1):  # 文章 -口袋看点
                    headers = {
                        'Host': 'mi.adhbio.cn',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN',
                        'Accept': '*/*',
                        'Accept-Encoding': 'gzip, deflate, sdch',
                        'Accept-Language': 'zh-CN,zh;q=0.8',
                        'Referer': 'http: // mi.adhbio.cn / c11823 - 26380.html?from=singlemessage',
                        'X - Requested - With': 'XMLHttpRequest',
                        'Cookie': 'UM_distinctid=16071e2d0b6baa8-0dcfc00a134596-33695a35-445c0-16071e2db6d97; CNZZDATA1262708615=63701390-1513738998-%7C1513738998; Hm_lvt_8d42a454b99f7403d0d4dc7a3d2dcbab=1513739181; Hm_lpvt_8d42a454b99f7403d0d4dc7a3d2dcbab=1513739199'}

                if (self.is_use_proxy):
                    print('【时间 {}】本次运行代理共{} 个，正在进行第{}个代理访问，代理ip为：{}。'
                          .format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), len(ips_all), index + 1, ip))
                    r = requests.get(url, headers=headers, proxies=proxies, timeout=8)
                    print('【运行结果】：{}\n'.format(r.status_code))
                    if r.status_code == 200:
                        success_count += 1
                        # print(r.content.decode('utf-8'))
                        # print(r.text)
                else:
                    r = requests.get(url, headers=headers)
                    print('【时间 {}】本次运行并未使用代理'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                    print('【运行结果】：{0}\n'.format(r.status_code))
                    if r.status_code == 200:
                        success_count += 1
                        # print(r.content.decode('utf-8'))
                        # print(r.text)
            except BaseException as ex:
                print("【运行结果】=> 出错：{0}\n".format(ex))
                fail_count += 1
                continue
        time.sleep(random.randint(0, 1))  # 爬完一个相册之后等待2-5秒再爬，防止反爬虫
        print('运行结束,本次运行代理总数：{}，成功数量为：{}，失败数量为：{}'.format(len(ips_all), success_count, fail_count))

    # 通过 selenium + phantomjs【测试】
    def get_request_byselenium_test(self):
        url = self.url
        # driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe') # windows环境下路径前加 r !!!
        # 千万注意是hromedriver.exe(驱动文件)，不是chrome 也可用firefox等其他浏览器
        driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe')
        driver.get(url)
        # driver.set_window_position(x=50, y=60) # 设置浏览器窗口的起始位置
        # driver.set_window_size(width=1366, height=700) # 设置浏览器窗口的大小
        elem = driver.find_element_by_id("kw")  # 获取元素
        elem.send_keys("同程旅游")  # 赋值
        # elem.send_keys(Keys.RETURN)
        driver.find_element_by_id('su').click()  # 百度搜索按钮事件
        print(elem.get_attribute('maxlength'))  # 获取属性

        # # 可以获取搜索结果页面的数据
        curr_url = driver.current_url  # 搜索结果页的地址
        driver.get(curr_url)  # 获取搜索结果内容
        time.sleep(2)
        print(driver.page_source)

        # elem = driver.find_elements_by_class_name("showMore").click()

    # 通过 selenium + phantomjs【文章最好用这种，更加真实，电影的后期也可以考虑用这个】
    def get_request_byselenium_formal(self):
        url = self.url

        # 设置请求头
        # 1、phantomjs 设置请求头
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = (
            "Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN"
        )

        # 2、chrome设置请求头
        # 进入浏览器设置
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('host=mi.tianshitonghe.cn')
        chrome_options.add_argument('connection=keep-alive')
        chrome_options.add_argument('upgrade-insecure-requests=1')
        chrome_options.add_argument('accept-encoding=gzip, deflate')
        chrome_options.add_argument('lang=zh-CN,en-US;q=0.8')
        chrome_options.add_argument(
            'accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/wxpic,image/sharpp,*/*;q=0.8')
        chrome_options.add_argument(
            'user-agent="Mozilla/5.0 (Linux; Android 6.0.1; 1505-A02 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043613 Safari/537.36 MicroMessenger/6.5.22.1160 NetType/WIFI Language/zh_CN"')

        success_count = 0
        fail_count = 0
        try:
            if self.is_use_proxy:
                ips_all = self.read_proxyips()
                js = "$('.showMore').click();alert(1)"
                for index, http_address in enumerate(ips_all):  # 列表加了enumerate 可以访问索引
                    try:
                        # chromeOptions.add_argument('--proxy-server=http://ip:port')
                        http_type = http_address['http_type']
                        ip = http_address['ip']
                        chrome_options.add_argument('--proxy-server={}://{}'.format(http_type, ip))  # 设置代理
                        # driver = webdriver.PhantomJS(executable_path=r'D:\phantomjs-2.1.1-windows\bin\phantomjs.exe',
                        #                           desired_capabilities=dcap)
                        driver = webdriver.Chrome(executable_path=r'D:\chromedriver_win32\chromedriver.exe',
                                                  chrome_options=chrome_options)
                        print('【时间 {}】本次运行代理共{} 个，正在进行第{}个代理访问，代理ip为：{}。'
                              .format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), len(ips_all), index + 1,
                                      ip))
                        driver.get(url)
                        # js = "$.get('viewdata.php?aid=11823&uid=26380&pv=33)"
                        driver.execute_script(js)  # 立即执行js,触发记录访问量的程序
                        success_count += 1
                        print('【运行结果】：{}\n'.format('未知1'))
                    except BaseException as ex:
                        print("【运行结果】=> 出错：{0}\n".format(ex))
                        fail_count += 1
                        continue
                    time.sleep(2)
            else:
                driver = webdriver.Chrome(executable_path=r'D:\chromedriver_win32\chromedriver.exe',
                                          # desired_capabilities=dcap,
                                          chrome_options=chrome_options)
                driver.get(url)
                js = "$('.showMore').click()"
                driver.execute_script(js)
                print('【时间 {}】本次运行并未使用代理'.format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
                print('【运行结果】：{0}\n'.format('未知2'))
        except BaseException as ex:
            print("【运行结果】=> 出错：{0}\n".format(ex))

        print('运行结束,本次运行代理总数：{}，成功数量为：{}，失败数量为：{}'.format(len(ips_all), success_count, fail_count))

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
# AddVisit('http://mi.tianshitonghe.cn/c11823-26380.html?from=singlemessage', True).get_request_movie()
# AddVisit('http://mi.adhbio.cn/viewdata.php?aid=11823&uid=26380&pv=37', True).get_request_article(1)

# AddVisit('http://www.baidu.com', False).get_request_byselenium_test()
AddVisit('http://mi.tianshitonghe.cn/c12080-26380.html?from=singlemessage', True).get_request_byselenium_formal()
