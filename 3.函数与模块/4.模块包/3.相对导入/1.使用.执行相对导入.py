#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    python总是在搜索路径中查找包，相对导入时python对from语句的扩展，用于模块文件中使用相对路径导入宝中的模块。在模块的包
路径中，“.”表示包含了from导入命令的模块文件所在路径的上一级目录
'''
'''使用.执行相对导入'''
'''在mypysrc包中有模块文件reltest.py文件，内容如下'''
#E;\pytemp\mypysrc\reletest.py
#import os
#print(os.getcwd())#打印当前目录
#from .db.test import show          #使用相对路径导入
