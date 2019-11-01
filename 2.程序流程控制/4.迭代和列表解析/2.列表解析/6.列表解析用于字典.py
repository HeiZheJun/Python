#/usr/bin/python3
#-*- coding:utf-8 -*-
z = {x:ord(x) for x in 'abcd'}
print(z)
z = {x:ord(x) for x in 'abcd' if ord(x)%2==0}
print(z)