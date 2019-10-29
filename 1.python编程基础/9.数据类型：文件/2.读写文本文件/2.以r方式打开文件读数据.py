#/usr/bin/python3
#-*- coding:utf-8 -*-
'''以r方式打开文件时，只能读取文件的数据'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt')  #以默认方式打开文件
x = myfile.read()                              #读取全部文件到字符串
print(x)                                       #打印文件内容

print(myfile.read())                           #指针以指向文件末尾，返回为空

myfile.seek(0)                                 #将文件指针移到文件开头

print(myfile.read(5))                          #读5个字节到字符串

print(myfile.tell())                           #返回文件指针的当前位置

print(myfile.readline())                       #读取一行的内容因为指针在6，所以读取这一行6之后的内容
print(myfile.readline())                       #读取下一行
myfile.seek(0)
print(myfile.readlines())                      #读取全部内容到列表
myfile.seek(0)
for x in myfile:                               #以迭代的方式读文件
    print(x)
myfile.close()                                 #关闭文件
