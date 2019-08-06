#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''python在math模块中提供了大量的数学函数，使用之前要导入math函数'''
'''导入math函数模块'''
import math

'''数学常量π'''
print(math.pi)

'''数学常量e'''
print(math.e)

'''math.inf浮点数的正无穷大，-math.inf浮点数的负无穷大'''
print(math.inf)
print(-math.inf)

'''math.ceil(x)返回不小于x的最小整数'''
print(math.ceil(6.9))

'''math.fabs(x)返回x的绝对值'''
print(math.fabs(-5))

'''math.factorial(x)返回非负数x的阶乘'''
print(math.factorial(5))

'''math.floor(x)返回不大于x最大整数'''
print(math.floor(5.1))

'''math.fmod(x,y)返回x除以y的余数'''
print(math.fmod(8,3))

'''求和sum()函数由于浮点数的原因存在不精确性'''
'''math.fsum()sum更精准'''
x = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print(sum(x))
print(math.fsum(x))

'''math.gcd(x,y)返回x和y的最大公约数'''
print(math.gcd(12,8))

'''math.trunc(x)返回x的整数部分'''
print(math.trunc(15.56632))

'''math.exp(x)返回e的x次方'''
print(math.exp(5))

'''math.expm1(x)返回e的x次方减1'''
print(math.expm1(5))