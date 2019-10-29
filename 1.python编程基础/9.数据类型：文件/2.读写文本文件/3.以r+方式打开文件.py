#/usr/bin/python3
#-*- coding:utf-8 -*-
'''以r+方式打开文件时，可从文件读取数据或者向文件写入数据，在写入数据前，应先识用seek（）方法设置数据的写入位置
如果在read（）等方法读出数据后执行写入操作，数据会首先写入文件末尾'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt','r+')  #以r+方式打开文件,指针指向文件开头
x = myfile.write('hello')           #写入5个字符到文件的开头
myfile.seek(0)                      #定位指针到文件开头
print(myfile.read())                #读出全部数据
myfile.seek(7)                      #将指针指向第八个字节(位置为7)
myfile.write('123')                 #写入数据
myfile.seek(0)                      #定位指针到文件开头
print(myfile.read())                #读出全部数据
myfile.seek(0)                      #定位指针到文件开头
print(myfile.read(5))               #读出5个字符
myfile.write('这就是末尾了吗')    #写入数据在读出后理解写入数据，会写入在文件末尾
myfile.seek(0)                      #定位指针到文件开头
print(myfile.read())                #读出全部数据，看看写入是不是在末尾
myfile.close()                      #关闭文件



