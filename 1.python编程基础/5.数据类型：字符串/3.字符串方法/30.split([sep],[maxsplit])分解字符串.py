#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''将字符串按着sep指定的分隔字符串分解，返回分解后的列表
sep省略时以空格作为分隔符，maxsplit指定分解次数'''

x = 'aa bb cc dd ee'
print(x.split())

z = 'aa bb cc dd bb dd '
print(z.split('bb'))

print(x.split(maxsplit= 1))