#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
breack用于跳出当前循环，级提前结束循环（包括跳过else）。continue语句则用跳过循环体剩余语句
回到循环开头开始下一次迭代
'''
a = []
n = 0
for x in range(100,999):
    s = str(x)
    if s[0]!=s[-1]:
        continue
    a.append(x)
    n+=1
    if n==10:
        break
else:
    print('loop over')
print(a)