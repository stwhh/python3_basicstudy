#-*-coding:utf-8-*-


# # 1.列表 []标识
# 列表是有序的
# list=['a','b',2,'你好']
# print('开始列表：')
# for i in list:
#     print('\t'+str(i))
#
# # 添加
# list.append('我是追加的')
# list.insert(1,'我是插入的，第二个')
# print('添加后的列表：')
# for i in list:
#     print('\t'+str(i))
#
# # 修改
# list[0]='修改A'
# print('修改的列表：')
# for i in list:
#     print('\t'+str(i))
#
# # 删除
# # 删除指定索引
# del list[0]
# print('del 删除的列表1：')
# for i in list:
#     print('\t'+str(i))
#
# # 删除最后一个，并返回最后一个
# last = list.pop() # 可以带索引，删除指定索引的值并弹出这个值，比如pop(0),就是删除第一个元素并弹出
# print('del 删除的列表2：')
# for i in list:
#     print('\t'+str(i))
# print(last)
#
# # 根据值删除（如果出现多次，只删除第一个，需要循环才能都删除）
# list.remove(2) # 可删除指定值
# list.remove('b') # 删除指定值
# print('remove 删除的列表：')
# for i in list:
#     print('\t'+str(i))


# 列表解析
# 语法 [expression for iter_val in iterable if cond_expr]
squares =[item**2 for item in range(1,11)]
print(squares)
print(sum(squares))

squares =[item**2 for item in range(1,11) if item%2==0]
print(squares)
print(sum(squares))


# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4]) # 从0，开始到第三个结束
print(players[-1:]) # 最后1名
print(players[-3:]) # 最后3名


