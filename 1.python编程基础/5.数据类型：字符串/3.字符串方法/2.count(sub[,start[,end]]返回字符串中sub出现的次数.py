#/usr/bin/python
#-*- coding:UTF-8 -*-
'''count(sub[,start[,end]])返回字符串sub在字符串x的[start,end]范围内出现的次数，省略范围时查找整个字符串'''
x = 'abcdbacedca'
print(x.count('a',0,6))
print(x.count('a'))