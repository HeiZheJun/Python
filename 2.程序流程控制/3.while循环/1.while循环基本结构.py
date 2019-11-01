#/usr/bin/python3
#-*- coding:utf-8 -*-
'''while循环基本结构
while 测试条件：
    循环体
else：
    语句块
'''
'''与for循环类似，在循环体中使用break和continue语句，else部分可以省略'''

'''while循环执行时，首先计算测试条件，若成立则执行循环体中的语句，否则结束循环
循环体中语句执行完毕后，再次计算测试条件，若条件成立则继续执行循环体，否则循环结束'''
s = 0
n = 1
while n <=100:
    s +=n
    n+=1
print('1+2+3+4+...+100=',s)

'''在while循环中，else部分的语句在结束正常循环时执行，可在while循环中使用break跳出循环'''
'''使用while循环来输出100内的素数'''
x = 2
while x < 100:
    n = 2
    while n<x-1:
        if x%n==0:
            break
        n+=1
    else:
        print(x,end=' ')            #正常结束循环是说明x没有被任何数整除，是素数输出
    x+=1
else:
    print('over')