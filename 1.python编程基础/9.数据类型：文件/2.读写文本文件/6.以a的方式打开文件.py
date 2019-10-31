#/usr/bin/python3
#-*- coding:utf-8 -*-
'''以a方式发开文件时，写入的数据会追加到文件末尾'''
myfile=open(r'C:\Users\azhe\desktop\123.txt','a')       #以a方式打开文件
myfile.write('open the window')                         #将字符串写入文件
myfile.close()                                          #关闭文件
myfile=open(r'C:\Users\azhe\desktop\123.txt','r')       #以r方式打开文件
print(myfile.read())
myfile.close()                      