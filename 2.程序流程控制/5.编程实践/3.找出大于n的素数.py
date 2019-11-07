#/usr/bin/python3
#-*- coding:utf-8 -*-
'''输入任何一个正整数n，并找出大于n的最小素数'''
'''添加了判断是否为整数的语句'''
m=input('请输入整数：')
if m.isdigit():         #判断输入的是否是整数
    n = int(m)          #把输入的整数由str类型转换为int
    while True:         #无限循环
        n += 1
        # print(n)
        f = True
        a = 2
        while a < n - 1:        #判断是否为素数，不是的话循环，是的话继续下一个语句
            if n % a == 0:
                f = False
                break
            a += 1
        if f:
            print('大于%s的最小素数是%d' % (m, n))
            break
else:
    print('你输入的数字不是整数')
