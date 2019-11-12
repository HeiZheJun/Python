#/usr/bin/python3
#-*- coding:utf-8 -*-
'''全局变量不经定义即可在函数中使用，当在函数内部给变量赋值时，该变量疆内python视为局部变量
为了在函数内部给全局变量赋值，python提供了global语句，用于在函数内部生命全局变量
'''
a= 10
def show():
    global a                    #生命a是函数外的全局变量
    print('a=',a)
    a=100
    print('in show():a=',a)
show()
print(a)                        #因为声明了a是全局变量，所以代码中使用的a都是全全局变量a