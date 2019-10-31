#/usr/bin/python3
#-*- coding:utf-8 -*-
'''可以使用range（）生成包含连续多个整数的range对象,格式如下'''
'''
range(end)
range(start,end[,step])
只指定end参数时，生成整数范围为0~end-1  指定start时，整数范围为start~end-1 间隔为step，默认为1
'''

for i in range(4):
    print(i)
for i in range(3,13,2):
    print(i)