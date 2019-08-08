#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''字符串常量可以用多种方法表示'''
'''单引号，双引号，三个单引号和三个双引号'''
'''带r或R前缀的Raw字符串，r'abc\n123',R'abc\n123'。'''
'''带u或U前缀的Unicode字符串，u'abc\n123',U'abc\n123'。'''
'''字符串都是str类型的对象，可用内置str函数来创建字符串对象'''
x = str(123)
'''测试字符串类型'''
print(type(x))
'''用字符串常量创建字符串对象'''
x = str(u'abc')
print(x)
