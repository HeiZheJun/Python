#/usr/bin/python3
#-*- coding:utf-8 -*-
'''python允许嵌套使用for循环，即在for循环内部也可以视同for循环'''
'''输出100以内的素数，除了1和本身不能被其他证书整除'''
print(2,3,end=' ')               #二三是素数没直接输出，end=''使后续输出不换行
for i in range(4,100):
    for x in range(2,i):
        if i%x==0:              #若余数为0，说明i不是素数，结束当前for循环
            break
    else:
        print(i,end=' ')
print('happl end')



