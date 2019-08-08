#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''在Raw字符串中，python不会解释其中的转义字符，
Raw的字符串的典型应用是用来表示系统路径的'''
'''open语句视图打开时，会将字符串的\t之类情况处理为转义字符，从而导致出错'''
# mf = open('E:\BaiduNetdiskDownload\tatabase.txt','a')
'''为避免这种情况，我们可以添加反斜线表示转义字符'''
mf = open('E:\\BaiduNetdiskDownload\\tatabase.txt','a',encoding='UTF-8')
'''最简单的方法是使用Raw字符串'''
lf = open(r'E:\BaiduNetdiskDownload\test.txt','a',encoding='UTF-8')
'''或者使用反斜线代替'''
rf = open('E:/BaiduNetdiskDownload/a.txt','a',encoding='UTF-8')
print('人生苦短\n我用python',file=lf)