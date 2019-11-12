#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python允许在函数内部定义函数
内部定义的函数，只能在内部使用
'''
def add(x,y):
    def getsun(c):                  #在函数内部定义函数，将字符串转化为ASCII求和
        s=0
        for n in c:
            s+=ord(n)
        return s
    return getsun(x)+getsun(y)      #调用内部定义的函数getsun
print(add('1','3'))                 #调用函数