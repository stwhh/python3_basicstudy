# -*-coding:utf-8-*-
import re
from _datetime import datetime, timedelta
import json

# 取出de
# a = 'abcdefg'
# print(a.index('a'))
# print(a.index('b'))
# start_index = a.index('bc')
# end_index = a.index('fg')
#
# print(a[start_index + len('bc'):end_index])


# 正则表达式
# # match() 匹配成功返回match对象,否则返回None
# s = re.match(r'\d{3,5}-\d{5,8}', '010-666666')
#
# print(s)
# if (s == None):
#     print('匹配失败')
# else:
#     print('匹配成功')
#
#
# s='<a class="mm-first" href="//mm.taobao.com/self/album_photo.htm?user_id=176817195&album_id=10000878652&album_flag=0" target="_blank"> <img src="//img.alicdn.com/imgextra/i1/176817195/TB1bmwwKpXXXXXaXpXXXXXXXXXX_!!0-tstar.jpg_240x240xz.jpg" width="125" height="125"> </a> <!--<a class="mm-first" href="//mm.taobao.com/self/album_photo.htm?user_id=176817195&album_id=10000878652&album_flag=0" target="_blank"> <img src="//img.alicdn.com/imgextra/i4/176817195/TB15bsVKFXXXXbuaXXXXXXXXXXX_!!0-tstar.jpg_250x250.j'
# # pattern='href="//mm.taobao.com/self/album_photo.htm?user_id=176817195&album_id=(.*?)&album_flag=0'
# # pattern2=re.compile('href="//mm\.taobao\.com/self/album_photo\.htm\?user_id=176817195&album_id=(.*?)&album_flag=0')
# pattern2=re.compile('href="//mm\.taobao\.com/self/album_photo\.htm\?user_id=176817195&album_id=(.*?)&album_flag=0')
# urls=re.findall(pattern2,s)
# for i in urls:
#     print(i)




# 查找所有符合条件的数据
# s2=re.findall(r'\d{3,5}', '010-abc345-d678jdeg57654jd87kal8e77a8e')
# print(s2)


# finditer用法，暂时不掌握
# s3=re.finditer(r'\d{3,5}', '010-abc345-d678jdeg57654jd87kal8e77a8e')
# print(s3)

print(datetime.now())

dt=datetime(2018,12,1,12,34,23)

print(dt)
print(type(dt))

timestamp=dt.timestamp()
print(timestamp)

time=datetime.fromtimestamp(timestamp) # 本地时间
print(time)

utctime=datetime.utcfromtimestamp(timestamp) # 格林威治时间
print(utctime)

# # str转成时间
# cday=datetime.strptime('2017-5-6 12:23:34','%Y-%m-%d %H:%M:%S') # 后面的参数必须跟时间格式一致，参数必须要
# print(cday)
#
# print(time.strftime('%Y-%m-%d %H-%M-%S'))


# 时间加减
time_add=time+timedelta(days=3)
print(time_add)
#
#
#
#
# #对象序列号
# dic={'no':'12458','name':'孙涛'}
# dic_json=json.dumps(dic)
# print(dic_json)
#
# dic2=json.loads(dic_json)
# print(dic2)


# 异常处理+while循环
def test():
    i = 0
    while i < 5:  # 只循环5次
        s = input('请输入被除数！')
        try:
            rst = 10 / int(s)
        except ZeroDivisionError:
            print('不能输入0')
        except ValueError:
            print('值无效')
        else:
            print(rst)
        i += 15


# test()
