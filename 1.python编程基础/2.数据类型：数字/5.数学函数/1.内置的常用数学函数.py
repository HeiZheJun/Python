#/usr/bin/python3
#-*- coding:UTF-8 -*-

'''求绝对值'''
print(abs(-5))

'''将整数转化为二进制字符'''
print(bin(5))

'''返回整数的十六进制字符串'''
print(hex(20))

'''返回整数的八进制字符串'''
print(oct(20))

'''返回整数对应的ASCII码的字符'''
print(chr(65))

'''返回字符的ASCII码对应的整数'''
print(ord('A'))

'''返回商和余'''
print(divmod(9,4))

'''返回字符串中表达式的值'''
a = 5
print(eval('a*a+1'))

'''返回最大值'''
print(max(1,23,4,52))

'''返回最小值'''
print(min(1,23,4,52))

'''pow（x,y）返回x的y次方，等效x**y'''
print(pow(7,8))

'''四舍五入，只有一个参数时四舍五入为整数'''
print(round(1.56))

'''四舍五入，保留制定位数的小数'''
print(round(1.567,2))

'''四舍五入，舍入的部分刚好是5时，像偶数舍入'''
print(round(1.5),round(-1.5))