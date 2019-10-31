#/usr/bin/python3
#-*- coding:utf-8 -*-
'''w+与w方式的唯一区别是前者除了允许写文件，还可以读文件'''
myfile=open(r'C:\Users\azhe\desktop\123.txt','w+')
myfile.write('opne the door\n')
myfile.write('12345')
myfile.seek(0)                      #指针移到开头
print(myfile.readline())            #读第一行
print(myfile.readline())            #读下一行
print(myfile.readline())            #已经读到文件结尾，返回空字符串
myfile.seek(14)                     #将文件指针移到15
myfile.write('zero one two there four five')
myfile.seek(0)
print(myfile.read())                #读出全部文件
myfile.close()                      #关闭文件