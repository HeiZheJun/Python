#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''从字符串的开头，依次将包含的old字符串替换为new字符串，省略count时全部替换old字符串
指定count时，天次数不能大于count'''
x = 'abc123'*4
print(x.replace('ab','ad'))
print(x.replace('ab','ad',(2)))