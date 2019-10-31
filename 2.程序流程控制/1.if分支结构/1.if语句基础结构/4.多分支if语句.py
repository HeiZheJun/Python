#/usr/bin/python3
#-*- coding:utf-8 -*-
'''多分支if语句由 if、一个或多个elif和else组成，else可省略'''
x = 80
if x<60 :
    print('不及格')
elif x<70:
    print('及格')
elif x<90:
    print('中等')
else:
    print('优秀')

'''python在执行多if分支是，按着先后顺序依次计算各个测试表达式，当前面的测试表达式为假时，才会计算下一个表达式，否则
执行相应的语句块，语句块执行完则if语句结束，不在计算后面的表达式，如果所有的表达式均为假时，则会执行else部分语句'''