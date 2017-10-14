# -*-coding:utf-8-*-

# 无参数的装饰器
def log_noargs(func):
    def wrapper(*args, **kwargs):
        print("【无参数装饰器】调用了方法：{}()".format(func.__name__))
        # print("调用了方法：%s()" % func.__name__)
        return func(*args, **kwargs)

    return wrapper


# 有参数的装饰器
def log_had(text):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            print("【有参数装饰器】调用了方法：{}(),参数为：{}".format(func.__name__, text))
            # print("调用了方法：%s()" % func.__name__)
            return func(*args, **kwargs)
        return wrapper2

    return wrapper1


@log_noargs
def my_method():
    print("方法1在这：")


@log_had('st')
def my_method2():
    print("方法2在这：")


my_method()
my_method2()
# log_had('孙涛')(my_method2)
