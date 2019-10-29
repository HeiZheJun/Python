#/usr/bin/python3
#-*- coding:utf-8 -*-
'''values()方法返回字典中全部值得视图'''
x={'name':'zhemei','sex':'man'}
print(x)                            #返回键值对视图
y=x.values()                        #显示值得视图，值视图为dict_values对象
print(y)

x['age']=22                         #为字典添加键值对
print(x)                            #显示结果表明添加了键值对
print(y)

print(list(y))                      #将视图转换为列表