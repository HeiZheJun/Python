#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''集合（set）常量与字典类似，用花括号表示{1,2,3}，集合中的元素是唯一的、无序的、不可改变的。
集合支持数学理论中的各种集合运算'''

'''常量集合'''
'''集合常量用或括号表示，可以用内置的函数set来创建'''
'''直接使用集合常量'''
x={1,2,3}
print(x)
print(type(x))
'''使用集合常量做参数创建集合对象'''
y = set({1,2,3})
'''使用列表常量做参数创建集合对象'''
r = set([1,2,3,])
'''使用字符串常量做参数创建集合'''
z = set('abcdefghijklmnopqrstuvwxyz')
'''创建新的集合'''
c = set()
'''{}表示空的字典对象'''
type({})

'''集合中的元素不允许有重复值，在创建集合对象的时候，python会自动去掉重复值'''
print({1,1,2,2,3,3,4})
x = set([1,1,2,2,3,3,4,4])
print(x)
#{x for x in [1,2,3,4]}
#{1,2,3,4}
'''用解析对象的表达式来创建几个元素'''
#{x ** 2 for x in [1,2,3,4]}
#{16,1,4,9}
