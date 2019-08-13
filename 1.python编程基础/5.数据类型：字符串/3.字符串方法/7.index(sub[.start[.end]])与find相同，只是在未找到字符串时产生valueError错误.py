#/usr/bin/python
#-*- coding:UTF-8 -*-
'''与find（）方法一样，只是在未找到字符串时产生valueError错误'''
x = 'abcdcdsa'
print(x.index('ab'))
print(x.index('ab',2))