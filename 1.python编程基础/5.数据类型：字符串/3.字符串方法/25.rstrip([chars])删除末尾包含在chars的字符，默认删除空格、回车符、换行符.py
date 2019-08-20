#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''未指定参数chars阐述字符串末尾的空格、回车符、换行符，
否者删除字符串末尾包含在chars中的字符'''
x = 'a \n bc \n \r'
print(x.rstrip())
y = 'abc123abc'
print(y.rstrip('bc'))