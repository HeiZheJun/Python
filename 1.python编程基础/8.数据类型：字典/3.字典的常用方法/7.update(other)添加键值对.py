#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''添加键值对，参数other可以使另一个字典鬼用赋值格式表示的元组
若字典存在同名的键，则映射值被覆盖'''
x = {'name':'python','age':'20'}
x.update({'age':'30','sex':'male'})
print(x)
'''修改映射值'''
x.update({'sex':'Make'})
print(x)
'''添加键值对'''
x.update({'code':'120'})
print(x)