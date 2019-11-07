#/usr/bin/python3
#-*- coding:utf-8 -*-

import random       #导入生成随机素数的函数
n = 0
while n <10:                    #开始循环得的随机数符合下面的函数 只要n<10就一直循环
    x = random.randint(10,99)   #生成10-99的随机函数
    a=2                         #判断随机函数是不是素数
    while a < x -1 :
        if x % a == 0:
            break
        a+=1
    else:                       #是素数的话打印出来 n+1
        print(x,end=' ')
        n+=1
