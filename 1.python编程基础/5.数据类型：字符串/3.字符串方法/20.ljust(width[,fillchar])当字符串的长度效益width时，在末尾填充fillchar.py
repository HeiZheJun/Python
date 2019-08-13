#/usr/bin/python
#-*- coding:UTF-8 -*-
'''当字符串的长度小于width时，在字符串的末尾填充fillchar,默认填充空格
'''
x = 'abc'
print(x.ljust(7))
print(x.ljust(7,'6'))