#/usr/bin/python
#-*- coding:UTF-8 -*-
'''将字符串中的tab字符替换为空格'''
x = 'abc\tcde\tcac'
print(x)
print(x.expandtabs(tabsize=0))
print(x.expandtabs(tabsize=4))
print(x.expandtabs(tabsize=8))