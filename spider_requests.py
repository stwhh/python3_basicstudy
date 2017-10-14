# -*-coding:utf-8-*-

import requests


# 发起普通请求【登录测试成功】
def common_requests(url='http://www.jq22.com/emdl.aspx'):
    values = {'em': '656179572@qq.com', 'pw': 'wohouhui'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': url
    }
    r = requests.post(url, data=values, headers=headers)  # get请求把post改成get,data换成params=values
    # r2 = requests.get('http://www.jq22.com/myhome') # 这个就没有保持会话效果
    # # print(r.url)
    # # print(r.encoding)
    # # print(r.url)
    # print(r2.content.decode('utf-8'))
    print(r.content.decode('utf-8'))


# 用抓到的cookie登录博客园【用fiddler或者chrome把获取到的请求头都放上去，
# 经测试，去掉一个refer都不行,每次加密的密码也是不一样的，也得换】
def common_requests_cnblogs():
    url = 'https://passport.cnblogs.com/user/signin'
    datas = {
        "input1": "*************你自己的加密后的用户名，chrome或者fiddler抓包获取",
        "input2": "*************你自己的加密后的密码，chrome或者fiddler抓包获取",
        "remember": "false"
    }
    headers = {
        'Host': 'passport.cnblogs.com',
        'Origin': 'https://passport.cnblogs.com',
        'VerificationToken': '45fvhgTHELHGAUtP7AnGXDt4RTh_-wtGrah-IzEt7oSM9_hUU3LL_Oyj00wgH12cr9kv9IEbicrA8XuNA-jDfhztKAU1:3IKbYoI7imKAIJbYnBLFtjwOCLDwsC9aqle87HkB74eP1JuTMrXZutwxvIIdfXGEIBoTQXnoFMtEfEgtM3vKawIigDU1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': '你登录一次之后的Cookie'
    }
    # 请注意，data参数是form表单的数据，'Content-Type'必须为'application/x-www-form-urlencoded'
    # json参数是json数据，'Content-Type'必须为'application/json'
    r = requests.post(url, json=datas, headers=headers,
                      verify=False)  # get请求把post改成get,data换成params=values,verify=False跳过证书验证
    # r2 = requests.get('http://www.jq22.com/myhome') # 这个就没有保持会话效果
    # # print(r.url)
    # # print(r.encoding)
    # # print(r.url)
    # print(r2.content.decode('utf-8'))
    print(r.url)
    print(r.status_code)
    print(r.text)


# cookies
def get_cookies_request(url):
    r = requests.get(url)
    print(r.cookies)
    print(r.cookies['example_cookie_name'])


# 保持会话【测试成功】
def keepalive_requests(url='http://www.jq22.com/emdl.aspx'):
    s = requests.Session()
    values = {'em': '656179572@qq.com', 'pw': 'wohouhui'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': url
    }
    rst = s.post(url, data=values, headers=headers)
    print(rst.content.decode('utf-8'))
    r = s.get("http://www.jq22.com/myhome")
    print(r.content.decode('utf-8'))


# 代理
def requests_proxy():
    proxies = {
        "https": "http://41.118.132.69:4433"
    }
    r = requests.post("http://httpbin.org/post", proxies=proxies)
    print(r.text)


# 文件上传
def request_uploadfile():
    url = 'http://httpbin.org/post'
    files = {'file': open('D:\\123.txt', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)


# common_requests('http://www.jq22.com/emdl.aspx')
# keepalive_requests()
# request_uploadfile()

# get_cookies_request('https://www.baidu.com/')
common_requests_cnblogs()
