#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''该方法用于返回映射值或者字典添加键值对，指定键key在字典中存在时，返回映射值
若指定键key不存在，则添加key：default键值对，省略default时，默认映射值为None'''
x = {'name':'python'}
print(x.setdefault('name'))
print(x.setdefault('age',20))
print(x)