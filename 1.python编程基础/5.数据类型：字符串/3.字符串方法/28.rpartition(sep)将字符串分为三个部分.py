#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''rpartition和partition一样，只不过是从字符串的末尾开始找第一个sep'''
x = 'abc123abc123abc123'
print(x.rpartition('abc'))
print(x.rpartition('edg'))