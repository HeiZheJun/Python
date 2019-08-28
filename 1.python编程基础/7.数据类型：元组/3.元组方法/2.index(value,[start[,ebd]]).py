#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''index()方法用于在元组中查找指定的值，未使用start和end指定范围时
返回指定值在元组中第一次出现的位置，指定范围时，返回在指定范围内第一次出现的位置
元组不包含指定的值则出错'''
x = (1,2,3)*9
print(x.index(2))
print(x.index(2,3,6))