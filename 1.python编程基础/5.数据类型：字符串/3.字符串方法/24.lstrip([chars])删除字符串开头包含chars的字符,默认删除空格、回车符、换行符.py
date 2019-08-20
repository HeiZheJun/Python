#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''未指定参数的chars删除字符串开头的空格、回车符、换行符，
否则删除字符串开头包含 在chars中的字符'''
x = '\n \r  asdsac'
print(x.lstrip())
y = 'abcdefabc'
print(x.lstrip('bc'))