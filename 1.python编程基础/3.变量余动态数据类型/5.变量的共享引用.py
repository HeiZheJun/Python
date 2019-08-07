#/usr/bin/python
#-*- coding:UTF-8 -*-
'''共享引用指多个变量引用了一个对象'''
x = 9
y = x
'''实际上是y= 9'''
print(x,y)
x = 6
print(x,y)
'''更改了x的引用不影响y'''


'''当对象被共享引用时，修改的时对象，意味着所有引用了该对象的变量都会改变'''
x =[1,2,3,4,5,6]
y = x
print(x,y)

x[0]=6
print(x,y)

'''is 可以判断两个变量是否引用了同一个对象'''
x = 7
c = x
y = c
print(x is y)