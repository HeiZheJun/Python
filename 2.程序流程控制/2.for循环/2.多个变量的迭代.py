#/usr/bin/python3
#-*- coding:utf-8 -*-
'''可在for循环中使用多个变量迭代序列对象'''
for a,b in ((1,2),(3,4),(5,6)):
    print(a,b)
'''与赋值语句类似，可以用*给变量赋值一个列表'''
for (a,*b) in ((1,2,'abc'),(3,4,5),(5,6,7)):
    print(a,b)