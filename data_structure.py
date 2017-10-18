#-*-coding:utf-8-*-


# 1.列表
list=['a','b',2,'你好']
print('开始列表：')
for i in list:
    print('\t'+str(i))

# 添加
list.append('我是追加的')
list.insert(1,'我是插入的，第二个')
print('添加后的列表：')
for i in list:
    print('\t'+str(i))

# 修改
list[0]='修改A'
print('修改的列表：')
for i in list:
    print('\t'+str(i))

# 删除
# 删除制定索引
del list[0]
print('del 删除的列表1：')
for i in list:
    print('\t'+str(i))

# 删除最后一个，并返回最后一个
last = list.pop() # 可以带索引，删除制定索引的值
print('del 删除的列表2：')
for i in list:
    print('\t'+str(i))
print(last)

# 根据值删除（如果出现多次，只删除第一个，需要循环才能都删除）
list.remove(2) # 可以带索引，删除制定索引的值
list.remove('b') # 可以带索引，删除制定索引的值
print('remove 删除的列表：')
for i in list:
    print('\t'+str(i))




# 2.元组
