#/usr/bin/python3
#-*- coding:utf-8 -*-
'''在定义函数时，若参数名前面使用星号“*”，则表示可以接受任意个数的参数，这些参数保存在一个元组中'''
def add(a,*b):
    s=a
    for x in b:                 #用循环迭代元组b的数据
        s+=x                    #累加
    return s                    #返回累加的值
print(add(1,2))                 #求2个数的和
print(add(1,2,3,4,5,6))         #求多个数的和
