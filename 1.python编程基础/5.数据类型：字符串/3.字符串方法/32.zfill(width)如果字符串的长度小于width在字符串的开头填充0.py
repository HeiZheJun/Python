#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''如果字符串的长度小于width，则在字符串的开头填充0，使长度等于width
如果第一个字符为加号或者减号，则在加减号之后填充0'''

x = '123'
print(x.zfill(8))

z = '-123'
y = '+123'
print(z.zfill(8))
print(y.zfill(8))