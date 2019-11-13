#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    再导入模块时python会使用米快文件创建一个模块对象。模块中引用的各种对象的变量名称为对象的树形。python也为模块对象添加
了一些内置的树形，可使用dir函数来查看对象属性
'''
import test1                #导入模块
print(dir(test1))           #查看模块的属性
print(test1.__doc__)        #返回文件开头的文档注释
print(test1.__file__)       #返回模块的完整路径
print(test1.__name__)       #显示模块名称
'''dir（）函数返回的列表包含了模块对象的树形，其中以双下划线“__”为开头和结尾的是python内置的树形，其他未代码变量名'''