#/usr/bin/python
#-*- coding:UTF-8 -*-
'''判断字符串[start,end]范围内的字符串是否以sub为开头'''
x = 'abcdef'
print(x.startswith('a'))
print(x.startswith('a',0,5))
print(x.startswith('c',2,5))
