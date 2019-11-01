#/usr/bin/python3
#-*- coding:utf-8 -*-
'''一些函数中可直接使用可迭代对象'''
print(all([0,2,4,1,3,5]))       #所有对象都为真时返回false
print(any([0,2,4,1,3,5]))       #有一个对象为真时返回true
print(sum([0,2,4,1,3,5]))     #求和
print(sorted([0,2,4,1,3,5]))    #排序
print(min([0,2,4,1,3,5]))       #求最小值
print(max([0,2,4,1,3,5]))       #求最大值
print(min(open(r'C:\Users\azhe\Desktop\123.txt')))  #返回文件中所有行的最小值（按着字母顺序排列的）
print(max(open(r'C:\Users\azhe\Desktop\123.txt')))  #返回文件中所有行的最大值
print(list(open(r'C:\Users\azhe\Desktop\123.txt'))) #将文件内容转换为列表
print(set(open(r'C:\Users\azhe\Desktop\123.txt')))  #将文件内容转化为集合
print(tuple(open(r'C:\Users\azhe\Desktop\123.txt')))#将文件内容转化为元组
a=open(r'C:\Users\azhe\Desktop\123.txt')            #将文件内容转赋值给变量
print(a)
a,*b=open(r'C:\Users\azhe\Desktop\123.txt')         #将文件内容转赋值给变量
print(a,b)