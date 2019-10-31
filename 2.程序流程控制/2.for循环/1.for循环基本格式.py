#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
for var in object:
    基本语句块
else：
    语句块
'''
'''
else部分可以省略，for执行时，依次将可迭代对象object中的值赋值给变量var，var没赋值一次
则执行一次循环体语句块，循环执行结束时，如果有else部分则执行相对应的语句块，else本分只在正常结束循环时执行
如果break跳出循环，则不会执行else部分
'''
for i in range(11):
    print(i)

for x in 'hello mother fucker':
    print(x)

for i in (1,2,3):
    print(i*2)
else:
    print('hello mother fucker')
'''在迭代字典对象时，变量一次迭代字典的各个键'''
a ={'name':'zhemei','age':22}
for x  in a:
     print(x,a[x])

