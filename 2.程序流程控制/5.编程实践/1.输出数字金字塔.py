#/usr/bin/python3
#-*- coding:utf-8 -*-

for x in range(1,10):
    print(' '*(10-x),end='')    #打印空格
    n=x
    while n>=1:                 #输出前半部分内容，end是让输出的数字一行显示
        print(n,end='')
        n-=1
    n+=2                        #输出后半部分的内容
    while n<=x:
        print(n,end='')
        n+=1
    print()