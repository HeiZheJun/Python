#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''冻结集合是不可改变的集合'''
'''可作为其他集合的元素'''
x = frozenset([1,23,4])
'''冻结集合的打印方式与其他集合不同'''
print(x)

y =set([1,3,4])
print(y)

'''将冻结集合作为元素加入另一个集合'''
y.add(x)
print(y)