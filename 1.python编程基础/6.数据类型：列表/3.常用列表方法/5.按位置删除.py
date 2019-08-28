#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''pop()方法可删除指定位置的值，省略位置时删除列表最后一个对象，同时返回删除对象'''
x = [1,2,3,4,5]
x.pop()
print(x)
x.pop(0)
print(x)