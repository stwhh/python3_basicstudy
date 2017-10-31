# -*-coding:utf-8-*-

# 2.元组 () 表示
# 列表是可修改的，元组元素是不可修改的
# 元组是有序的

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 遍历
for i in dimensions:
    print(i)

# 元组元素不可修改，但是元组可以重新赋值
modify_dimensions = (400, 600)
print('修改之后的元组')
for i in modify_dimensions:
    print(i)
