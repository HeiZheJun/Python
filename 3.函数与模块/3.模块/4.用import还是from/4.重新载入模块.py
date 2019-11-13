#/usr/bin/python3
#-*- coding:utf-8 -*-
'''imp模块已弃用，取而代之的importlib模块'''
'''
    很多时候再次使用import和from导入模块的时候，其本意通常是重新执行模块代码，恢复相关变量到模块执行时的状态
显然这种愿望在使用import和from导入是无法达到的
    python在imp模块中提供了reload函数来重新载入并执行模块代码。使用reload重新载入模块时，如果模块文件被修改，则执行
修改后的代码
    reload函数用模块变量名作为参数，重载对应模块，所以reload重载的只是使用import已经导入的模块，如果模块还没有导入，这行
reload则会出错
'''
import test3        #导入模块
print(test3.x)
test3.x = 300
print(test3.x)
import test3        #再次导入
print(test3.x)      #再次导入没有影响之前的赋值
from importlib import reload        #导入reload
reload(test3)       #重载模块
print(test3.x)      #因为模块代码再次被执行，x被赋值为原始值


