#/usr/bin/python3
#-*- coding:utf-8 -*-
'''文件有自己的迭代器：_next_()方法,无元素返回时，会产生一个StopIteration异常'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt','r')
print(myfile.__next__())
print(myfile.__next__())
print(myfile.__next__())
'''也可以用next（）函数来调用文件对象的迭代器'''
print(next(myfile))
print(next(myfile))
print(next(myfile))
print(next(myfile))
