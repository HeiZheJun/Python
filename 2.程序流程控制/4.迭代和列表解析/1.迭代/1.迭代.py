#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python中的各种序列（字符串，列表，元组，字典以及文件等）均是可迭代对象，可迭代对象可以使用
迭代器来遍历包含的元素'''
'''字符串、列表、元组、以及字典等对象虽然是可迭代对象，但是他们没有自己的迭代器
python中使用iter（）函数来生成可迭代对象的迭代器，然后对迭代器调用next（）函数来遍历对象
next（）函数U依次返回可迭代对象的一个元素，无元素返回时，会产生一个StopIteration异常'''
d = iter([1,2,3])               #为列表生成迭代器
print(next(d))                  #返回第一个元素
print(next(d))                  #返回第二个元素
print(next(d))                  #返回第三个元素
#print(next(d))                  #无元素返回，产生异常

d=iter((1,2,(3,4)))             #使用贴带起迭代元组
print(next(d))
print(next(d))
print(next(d))
d=iter('abc')                   #使用迭代器迭代字符串
print(next(d))
print(next(d))
print(next(d))
d=iter({'name':'zhemei','age':22})  #使用迭代器迭代字典
print(next(d))
print(next(d))
d=iter({'name':'zhemei','age':22}.keys())   #迭代字典keys方法返回对象
print(next(d))
print(next(d))
d=iter({'name':'zhemei','age':22}.values()) #迭代字典values方法返回值
print(next(d))
print(next(d))
d=iter({'name':'zhemei','age':22}.items())  #迭代字典items方法返回对象和值
print(next(d))
print(next(d))