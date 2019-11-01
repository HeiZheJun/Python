#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python允许在while循环内部使用while循环，'''
'''输出九九乘法表'''
a = 1
while a<10:
    b = 1
    while b<=a:
        print('%d*%d=%d'%(b,a,a*b),end=' ')
        b+=1
    print()                               #为每个while a<10循环换行
    a+=1