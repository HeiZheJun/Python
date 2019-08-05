#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''再运到不同的数据类型参与运算时，python总是将简单的类型转化为复杂的类型'''
'''python中的类型复杂程度：布尔值比整数简单，整数比浮点数简单，浮点数比复数简单'''
print(2+3.5)
print(type(2+3.5))
print(type(2+3.5+(2+3j)))