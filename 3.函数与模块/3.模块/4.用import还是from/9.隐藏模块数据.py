#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    在使用from……import *导入模块变量时，默认会将模块顶层的所有变量名导入，例外情况是。以单个下划线为开头的变量如：_abc
不会被导入
'''
from test8 import *
print(show())
#print(_y)          #报错
'''
    可以看到，执行from……import*导入后，模块中的x、show被导入，而_y和_add没有导入
    可以在模块开头使用__all__变量设置from……import语句导入的变量名
'''
'''可以在模块的开头使用__all__变量设置使用from……import语句是导入变量名'''
'''例如在test8中添加__all__=['_y','_add','show']变量，test8模块中只有这3个变量会被导入'''
print(_y)
