#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''对象没有任何引用时，其占用的内存空间会自动被回收-称为自动垃圾回收
在内部，python为每个对象创建一个计数器，计数器记录对象的引用次数，
当计数器为0时，对象被删除，其占用的内存被回收'''
x = 5
print(type(x))

'''当变量x引用对象1.5时，对象5被祸首，并且数据类型改变，证明变量没有数据类型，数据类型属于对象'''
x = 1.5
print(type(x))

x = 'abc'
print(type(x))