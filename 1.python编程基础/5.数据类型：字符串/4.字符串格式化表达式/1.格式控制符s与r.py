#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''格式控制符s和r的作用 与函数str（）和repr（）相同，针对字符串对象，
r和repr（）得到的目标字符中会包含表示字符串的单引号——称为repr表达式'''
'''用s格式化整数浮点数和字符串'''
print('%s  %s   %s'%(123,1.23,'abc'))
'''用r格式整数浮点数和字符串，注意区别'''
'''会在字符串上添加单引号'''
print('%r   %r  %r'%(123,1.23,'abc'))
