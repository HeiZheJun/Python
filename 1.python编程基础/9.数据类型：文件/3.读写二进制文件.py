#/usr/bin/python3
#-*- coding:utf-8 -*-
'''二进制读写的是bytes字符串'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt','wb')      #以wb的方式打开文件
myfile.write(b'you is my son')                          #写入bytes字符串，二进制只能写bytes字符串

myfile.close()

myfile=open(r'C:\Users\azhe\Desktop\123.txt','r')
print(myfile.read())                                    #打印字符串

myfile.close()

myfile=open(r'C:\Users\azhe\Desktop\123.txt','rb')      #以rb的方式打开字符串
print(myfile.read())
myfile.close()                                          #打印bytes字符串