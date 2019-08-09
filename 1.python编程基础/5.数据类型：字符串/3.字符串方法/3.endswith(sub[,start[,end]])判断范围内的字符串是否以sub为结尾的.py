#/usr/bin/python
#-*- coding:UTF-8 -*-
'''判断字符串[start,end]范围内是否已sub为结尾'''
x = 'abcdef'
print(x.endswith('f'))
print(x.endswith('d'))
print(x.endswith('c',0,3))