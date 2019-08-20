#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''将字符串在sep第一次出现的位置分割为三部分：sep前、sep和sep后，返回一个三元组。
没有找到sep时返回字符串本身和两个空格组成的三元组'''
x = 'abc123abc123abc123'
print(x.partition('12'))
print(x.partition('de'))
