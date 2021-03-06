#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''整数常量就是不带小数点的书。如 123 -12 0 9999999999等。
整数理论上是可以无穷大的，只要计算机的内存空间足够'''
print(2**100)   #2的一百次方
print(9**100)   #9的一百次方

'''一般整数的常量为十进制，python还允许将整数常量表示为二进制、八进制、十六进制。'''
'''二进制以0b或者0B开头 后面跟二进制数字 （0或1）   0b01101'''
'''八进制以0o或者0O开头 后面跟八进制数字（0-7）    0o1235710'''
'''十六进制以0x或者0X开头 后面跟十六进制数字（0-9，A-F)  0x921574AD'''

'''可以使用int将一个字符串按指定的禁止转化为整数，必须是整数
格式：int('整数字符串',n)'''
print(int('111'))        #默认十进制
print(int('111',2))      #二进制转换
print(int('111',8))      #八进制转换
print(int('111',10))     #十进制转换
print(int('111',16))     #十六进制转换

'''内置函数bin(x) oct(x) hex(x) 可以用于整数转化为对应的进制字符串'''
print(bin(50))   #转化为二进制字符
print(oct(50))   #转化为八进制字符
print(hex(50))   #转化为十六进制字符
