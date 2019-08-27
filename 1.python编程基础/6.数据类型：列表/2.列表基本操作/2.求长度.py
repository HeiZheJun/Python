#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''可以使用len（）来获得列表的长度'''
x = [123,('abc',123),'12ac']
print(len(x))

'''使用迭代来获取'''
d = 0
for i in x:
    d+=1
print(d)