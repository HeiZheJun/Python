#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''items（）方法返回键值对视图'''
x={'name':'zhemei','sex':'man'}
print(x)                            #返回键值对视图
y = x.items()                       #显示键值的对视图，键值对视图为dict_items对象
print(y)
for i in y:print(i)                 #迭代键值对视图


x['sex']='girl'                     #修改词典

print(x)

print(y)                            #从显示结果可以看出视图反应字典修改的内容

print(list(y))                      #将键值对视图转换为列表


