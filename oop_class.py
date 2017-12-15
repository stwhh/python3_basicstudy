# -*-coding:utf-8-*-
class Person:  # 一个空的代码块
    """

    用户类
    """
    def __init__(self, name):
        """文档字符串-函数描述"""
        self.name = name
        print("我的名字是：" + name)

    def say_hi(self):
        """问候方法"""

        # print("你好:" + name)
        print("你好:{}".format(self.name))


# p = Person('孙涛')
# print(p.say_hi())
#
# print(Person('文荟').say_hi())


#打印文档字符串
print(Person.__doc__)
print(Person.say_hi.__doc__)