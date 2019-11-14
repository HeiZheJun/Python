#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
模块定义为一个函数库，包含另个函数供其他模块使用
函数yanghui(n)用于输出杨辉三角
'''
def yanghui(n):
    #限制杨辉三角的阶数
    if not str(n).isdecimal() or n<2 or n>25:
        print('杨辉三角函数yanghui(n),参数必须是不下雨2且不大于25的正整数')
        return False
    #使用列表对象来生成杨辉三角
    x = []
    for i in range(1,n+1):
        x.append([1]*i)
    #计算杨辉三角矩阵其他值
    for i in range(2,n):
        for j in range(1,i):
            x[i][j]=x[i-1][j-1]+x[i-1][j]
    #输出杨辉三角
    for i in range(n):
        if n<=10:
            print(' '*(40-4*i),end='')
        for j in range(i+1):
            print('%-8d'% x[i][j],end='')
        print()
'''代码结束'''

'''独立运行测试代码开始'''
if __name__=='__main__':
    print('模块独立运行测试输出')
    print('一，10阶杨辉三角如下：')
    yanghui(10)