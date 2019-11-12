#/usr/bin/python3
#-*- coding:utf-8 -*-
'''在test4和test5中包含了同名的变量名'''
from test4 import show          #导入test4中的函数show
from test5 import show          #导入test5中的函数show
show()                          #输出后显示的show
from test5 import show
from test4 import show
show()
'''
虽然导入了两个模块，但是后导入为show赋值，覆盖了前面的赋值，只能调用后面赋值时引用的模块函数
'''
'''如果使用import导入不会出现这种问题'''
import test4
import test5
test4.show()
test5.show()
