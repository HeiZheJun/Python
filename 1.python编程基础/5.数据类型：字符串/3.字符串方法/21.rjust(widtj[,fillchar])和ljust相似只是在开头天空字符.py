#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''当字符串的长度小于width时，在字符串的开头填充fillchar。使长度等于width，默认填充空格'''
x = 'abc'
print(x.rjust(7,'a'))
print(x.rjust(7))