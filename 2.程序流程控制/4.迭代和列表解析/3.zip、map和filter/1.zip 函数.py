#/usr/bin/python3
#-*- coding:utf-8 -*-
'''zip函数参数为多个可迭代对象，每次从每个可迭代对象中取一个值组成元组，知道可迭代值去玩，
生成的zip包含了一系列的元组'''
x =(zip((1,2,3),('one','two','three')))     #用两个元组参数来解析生成元组序列
print(next(x))
print(next(x))
print(next(x))              #无对象是会产生StopIteration异常

x = (zip('abc',(1,2,3)))        #使用一个字符串和一个元组作为参数
print(next(x))
print(next(x))
print(next(x))

x = (zip((1,2,3),'abc',['one','tow','three']))      #使用多个可迭代对象
print(next(x))
print(next(x))
print(next(x))