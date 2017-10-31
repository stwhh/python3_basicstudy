# -*-coding:utf-8-*-
from urllib import request


# 读取文件
def file_read():
    with open('D:\\123.txt', 'r') as f2:
        # print(f2.read()) #不会读取到每行末尾的\n空格
        while True:
            s= f2.readline();
            print(s.strip())
            if(s==''):
                break
        # print(f2.readlines())


# 追加文件
def file_append():
    with open('D:\\123.txt', 'a', errors='啊，出错了。') as f3:
        print(f3.writelines('这是追加的内容。'))


# 编辑文件[会覆盖之前的]
def file_write():
    f = open('D:\\123.txt', 'w')
    print(f.write("覆盖了之前的内容"))
    f.close()

# 保存流文件
def saveImg(imageURL, fileName):
    u = request.urlopen('https://www.cnblogs.com/')
    data = u.read()
    f = open(fileName, 'wb')
    f.write(data)
    print(u"正在悄悄保存她的一张图片为"+ fileName)
    f.close()


# file_read()
# file_append()
# file_write()
# file_read()

# imgUrl='https://img.alicdn.com/imgextra/i3/176817195/TB17IssKFXXXXa1apXXXXXXXXXX_!!0-tstar.jpg_620x10000.jpg';
# saveImg(imgUrl,'D:\\1.jpg')

file_read()