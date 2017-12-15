# -*-coding:utf-8-*-
from collections import OrderedDict

# # 字典 {} 键值对标识，多个可以用[{},{}]跟json的格式一样
# # 字典是无序的
#
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
# # 添加键值对
# emptydic = {}  # 创建空字典
# emptydic['xpoint'] = 24
# emptydic['ypoint'] = 52
#
# print(emptydic['xpoint'])
# print(emptydic['ypoint'])
#
# # 修改字典
# emptydic['xpoint'] = 100
# print(emptydic['xpoint'])
# print(emptydic['ypoint'])
#
# # 删除键值
# del emptydic['xpoint']
# print(emptydic)
# for key, value in emptydic.items():
#     print('key={},value={}'.format(key, value))
#
# # 遍历字典所有key和value
# for key, value in alien_0.items():
#     print('key={},value={}'.format(key, value))
#
# # 遍历所有key
# for key in alien_0.keys():  # 默认遍历所有的键，因此，如果将上述代码中的 for name in alien_0,结果不变
#     print('6.key={}'.format(key))
#
# # 遍历所有value
# for key in alien_0.values():
#     print('7.value={}'.format(key))
#
# # 按顺序遍历
# alien_0['xpoint'] = 75
# print('顺序')
# for key in sorted(alien_0.keys()):
#     print(key)
#
# print('倒序')
# for key in sorted(alien_0.keys(), reverse=True):
#     print(key)
#
# # 字典列表(字典存在列表中)
# # alien_0 = {'color': 'green', 'points': 5}
# # alien_1 = {'color': 'yellow', 'points': 10}
# # alien_2 = {'color': 'red', 'points': 15}
# # aliens = [alien_0, alien_1, alien_2]
# # for item in aliens:
# #     print(item)
# #     # print(item['points'])
#
# # 直接定义字典列表
# allaliens = [{'color': 'green', 'points': 5},
#              {'color': 'yellow', 'points': 10},
#              {'color': 'red', 'points': 15}]
#
# for item in allaliens:
#     print(item)
#     # print(item['points'])
#
# # 添加字典到字典李列表
# allaliens.append({'xpoint': 23, 'ypoint': 45})
# for item in allaliens:
#     print(item)
#     # print(item['points'])
#
# # 列表存在字典里
# list_in_dic = {'姓名': 'st', '爱好': ['电脑', '音乐', '打球']}
# print(list_in_dic['姓名'])
# for item in list_in_dic['爱好']:
#     print(item)

# 字典中存储字典
users = {'st': {'年纪': 27, '住址': '江苏', '电话': '151*******'},
         'xh': {'年纪': 26, '住址': '中国', '电话': '131*******'}}
for key, values in users.items():
    print('姓名:' + key)
    print('\t年纪' + str(values['年纪']))
    print('\t住址' + values['住址'])
    print('\t电话' + values['电话'])

# message = input('请输入一个值：')
# print(message)

import  pymysql

users=455;
print(users)


# 有顺序的字典 OrderedDict
order_dic=OrderedDict()
order_dic['b']='12458'
order_dic['id']='655'
order_dic['c']='65'
order_dic['a']=7565
order_dic['4']=888
for i in order_dic:
    print(str(i)+'-'+str(order_dic[i]))
