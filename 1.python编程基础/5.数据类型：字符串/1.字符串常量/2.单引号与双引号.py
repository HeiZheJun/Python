#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''在表示字符串常量时，单引号和双引号没有区别，单引号中可以嵌入双引号，双引号中可以嵌入单引号'''
x = "abcdefg'123456"
y = 'abcdefg"123456'
print(x,y)
'''在交互模式下直接显示字符串时，默认用单引号表示，如果字符串中有单引号，则用双引号表示'''
