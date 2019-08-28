#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''字典通过键来索引映射的值'''
x = {'book':{'times':'30s','path':'c'},'python':20}
print(x['book'])
print(x['python'])
print(x['book']['times'])
'''可以通过索引来修改映射值'''
x['book']['times']='60s'
print(x)
'''使用修改不存在的键值对会添加键值对'''
x['apple']='pingguo'
print(x)