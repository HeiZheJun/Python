#/usr/bin/python3
#-*- coding:utf-8 -*-
'''列表解析用于文件时，依次从文件读取一行数据'''
z = [x for x in  open(r'C:\Users\azhe\Desktop\123.txt') ]
print(z)
z = [x.strip() for x in  open(r'C:\Users\azhe\Desktop\123.txt') ]
print(z)
z = [x for x in  open(r'C:\Users\azhe\Desktop\123.txt') if x[0]=='t']
print(z)