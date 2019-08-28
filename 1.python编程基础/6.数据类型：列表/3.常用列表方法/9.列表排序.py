#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''sort()方法可将列表中的对象排序，若列表对象全是数字，则按数字从小到大排序
若列表对象全是字符串，则按字典顺序排序，若列表包换多种类型，则会出错'''
x = [123,32,534,756,34,765]
x.sort()
print(x)
x = ['Acdf','Bsda','acsd','bsd']
x.sort()
print(x)