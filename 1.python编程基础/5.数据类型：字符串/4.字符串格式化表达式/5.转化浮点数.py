#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''在转化浮点数是%e、%g和%f略有不同'''
x = 12.3456789
print('%e   %g  %f'%(x,x,x))
print('%E   %G  %F'%(x,x,x))