#/usr/bin/python3
#-*- coding:utf-8 -*-
'''模块导入的基本格式，可以使用import或from语句来导入模块'''
'''
import 模块名字
import 模块名字 as 新名字
for 模块名字 import 导入对象名字
for 模块名字 import 导入对象名字 as 新名称
for 模块名字 import*
'''
'''import语句'''
'''import语句用于导入整个模块，可用as为导入的模块指定一个新的名称。使用import语句导入模块后，
模块中的对象均匀“模块名称.对象名称”的方式来引用'''
import  math                #导入模块
print(math.fabs(-5))        #调用模块函数
print(math.e)               #使用模块常量
#fabs(-5)                   #视图直接使用模块中的变量，出错
import math  as m           #导入模块并指定新名称
print(m.fabs(-5))
print(m.e)
print(math.fabs(-10))       #模块原名称也可以使用

'''from 语句'''
'''from语句用于指定导入模块中的指定对象，导入的对象直接使用，不需要使用模块名称作为限定符'''
from math import fabs       #从模块中导入指定的函数
print(fabs(-5))
from math import fabs as qwe    #导入时指定新名称
print(qwe(-10))

'''from……import*语句'''
'''使用*时，可导入模块顶层的全局变量和函数'''
from math import*
print(fabs(-5))
print(e)