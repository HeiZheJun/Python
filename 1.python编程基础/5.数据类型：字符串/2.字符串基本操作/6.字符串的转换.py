#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''可用str函数将整数、浮点数、复数转换为字符串'''
x = 123
x =str(x)
print(type(x))

x = 1.23
x =str(x)
print(type(x))

x = 2+3j
x =str(x)
print(type(x))

'''repr函数转换字符串，在转换数字式和str一样，
区别是在处理字符串时repr会将一对表示字符串常量的单引号添加到转换之后的字符串中'''
x = 123
print(str(x),repr(x))

x = '123'
print(str(x),repr(x))