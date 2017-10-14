# -*-coding:utf-8-*-
# from urllib import request, parse
from urllib import request, parse
import ssl


# 1.直接访问
def get_url(url):
    # 直接访问
    # req = request.urlopen('https://www.cnblogs.com/')
    # print(req.read().decode('utf-8'))

    # +异常处理+循环
    flag = False
    while flag == False:
        try:
            req = request.urlopen(url)
            print(req.read().decode('utf-8'))
        except:
            print('采集出错，将继续采集')
        else:
            flag = True
            print('采集结束')


# 2.构造request对象访问
def get_url_request():
    req = request.Request('https://www.cnblogs.com/')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))


# 伪造头访问
def get_url_request_header(url):
    data = parse.urlencode({'data': '1,0,0,0'}).encode('UTF8')  # 转成比特
    print(data)

    req = request.Request(url, data)
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Origin', 'https://www.cnblogs.com/')
    req.add_header('Referer', 'https://www.cnblogs.com/')
    # req.add_header('Referer', url)

    response = request.urlopen(req)
    print(response.read().decode('utf-8'))


# 3.post请求【登录测试成功】
def get_url_post(url='http://www.jq22.com/emdl.aspx'):
    values = {'em': '656179572@qq.com', 'pw': 'wohouhui'}
    data = parse.urlencode(values).encode('UTF8')  # post请求参数编码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'Referer': url}
    req = request.Request(url, data, headers)

    response = request.urlopen(req)
    print(response.read().decode('utf-8'))  # 这个网站登录成功返回Y,失败返回N,也可以验证必须要登录才能访问的网页


# 4.get请求,直接把参数写到网址上面或者用下面的方法
def get_url_get():
    values = {'username': 'stwhh', 'password': 'XXXX'}
    data = parse.urlencode(values)  # post请求参数编码
    get_url = 'https://www.cnblogs.com/' + '?' + data
    req = request.Request(get_url)  # 把参数字典编码成字符串形式拼接到url后面
    req.add_header('User-Agent',
                   'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    req.add_header('Origin', 'https://www.cnblogs.com/')
    req.add_header('Referer', 'https://www.cnblogs.com/')
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))


# 5.用代理访问
def get_url_Proxy():
    get_url = 'https://www.cnblogs.com/'
    proxy_handler = request.ProxyHandler({'http': '58.64.57.12:3128'})
    proxy_auth_handler = request.ProxyBasicAuthHandler()
    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
    opener = request.build_opener(proxy_handler, proxy_auth_handler)
    with opener.open(get_url) as f:
        print(f.read().decode('utf-8'))


# get_url()

# url='http://m.xiangjiaochang.cn/Go4ZoAO216388817745089.do?from=singlemessage';
# get_url_request_header(url)


# 模拟登陆这个网站
# url = 'http://www.jq22.com/emdl.aspx'
# get_url_post(url)


# get_url_request()
# get_url_Proxy()


# 下载文件
ssl._create_default_https_context = ssl._create_unverified_context
s = request.urlopen('https://pic4.40017.cn/line/admin/2016/09/26/15/ZVU9xR_640x360_00.jpg')
data = s.read()
f = open('D:\\2345.jpg', 'wb')
f.write(data)
f.close()

# req = request.Request('https://www.cnblogs.com/')
# # req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     # print('Data:', f.read().decode('utf-8'))


# s= [
#     ('username', 'email'),
#     ('password', 'passwd'),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ]
#
# s2={
#     'username': 'email',
#     'password': 'passwd',
#     'entry': 'mweibo',
#     'client_id': '',
#     'savestate': '1',
#     'ec': '',
#     'pagerefer': 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'
# }
#
# print(type(s))
# print(type(s2))
# print(parse.urlencode(s))
# print(parse.urlencode(s2))

