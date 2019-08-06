#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''分数对象明确的拥有一个分子和分母，分子和分母保持最简，
是用分数可以有效的避免浮点数的不确定性'''
'''分数使用fraction模块中的Fraction来创建，分数创建后可以用于各种计算'''
from fractions import Fraction
x = Fraction(2,8)
print(x)
print(x+2)
print(x-2)
print(x*2)
print(x/2)

'''可以使用浮点数转化为分数'''
y =Fraction.from_float(1.25)
print(y)