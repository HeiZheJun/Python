#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''创建字典'''
dict()  #创建空字典
{}      #创建空字典
x = {'name':'python','age':'20'}  #使用长量字典
z = {'nianji':{'32ban':'25ren','nan':'10','nv':'20'}}   #使用嵌套字典
y = {(1,3,5):9,(2,4,6):12}      #用元组作为字典
dict(name='python',age=25)      #使用赋值格式的键对创建字典
dict([('name','age'),('python',20)])    #使用包含元组和值元组的列表创建字典
dict.fromkeys(['name','age'])       #创建无映射值得字典，默认值为None
dict.fromkeys(['name','age'],0)     #创建值相同的字典
dict.fromkeys('abcd')               #使用字符串创建无映射值得字典
dict.fromkeys('abcd',10)        #使用字符串和映射值创建字典
dict(zip(['name','age'],['python',20]))     #使用zip解析键值列表创建字典


x = {}                  #创建空字典，通过赋值添加“键：值”对
x['name']='python'
x['age']=20
print(x)