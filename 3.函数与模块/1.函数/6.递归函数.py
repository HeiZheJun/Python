#/usr/bin/python3
#-*- coding:utf-8 -*-
'''递归函数是指在函数体内调用函数本身'''
def fnc(n):
    if n==0:
        return 1
    else:
        return n*fnc(n-1)       #递归调用函数本身
print(fnc(5))