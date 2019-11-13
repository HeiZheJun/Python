#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
python允许任何层次的嵌套导入模块。每个模块都是一个名字空间，嵌套导入意味着名字空间嵌套。在使用模块变量名时，则需要依次
使用模块变量名为限定符。例如：
'''
import test                     #导入模块test
print(test.x)                   #使用test模块变量
test.show()                     #使用test模块函数
print(test.test2.x2)            #使用嵌套调用的test2模块中的变量