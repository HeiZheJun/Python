#/usr/bin/python3
#-*- coding:utf-8 -*-
'''与for循环类似，在列表解析中也可以在for部分进行嵌套'''
z = [x+y for x in range(10) for y in range(100,110)]
print(z)
z=[x+y for x in (10,20) for y in (1,2,3)]
print(z)
'''嵌套时Python对第一个firewall迭代中的每个x，执行第二个for迭代y
用来嵌套的for循环来生成上面的列表'''
z = []
for x in (10,20):
    for y in (1,2,3):
        z.append(x+y)
print(z)
'''对于嵌套的解析，也可分别使用if来进行筛选'''
z=[x+y for x in (10,20) if x >10 for y in range(10) if y<8]
print(z)