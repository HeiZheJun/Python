#/usr/bin/python3
#-*- coding:utf-8 -*-
'''可以在列表解析结构的末尾使用if头部来执行筛选'''
t=[x+10 for x in range(10) if x%2==0 ] #使用if筛选偶数
print(t)
