#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''keys（）方法返回字典中所有键的视图'''
x={'name':'zhemei','sex':'man'}
print(x)                            #返回键值对视图
y = x.keys()
print(y)                            #返回键视图，视图为dict_keys对象


x['age']=22                         #为字典添加键值对
print(x)                            #显示结果表明添加了键值对
print(y)

print(list(y))                      #将视图转换为列表
