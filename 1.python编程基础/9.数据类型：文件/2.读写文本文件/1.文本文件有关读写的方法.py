#/usr/bin/python3
#-*- coding:utf-8 -*-
'''文本文件读写方法'''

'''
·myfile.read()              把整个文件内容读进一个字符串
·myfile.read(n)             把n个字符读进一个字符串
·myfile.readline()          把下一个换行符号之前的内容镀金一个字符串（读一行），读出内容包含行尾号
·myfile.readlines()         把整个文件内容读入一个字符串列表，每一行为一个字符串
·myfile.write(xstring)      将字符串写入到文件指针位置，返回写入的字符个数
·myfile.writelines(xlist)   将列表写入文件指针位置，返回写入的字符个数
·myfile.seek(n)             将文件指针移动到第n个字节。0表示文件的开头
·mufile.tell()              返回文件指针当前位置
·for line in myfile         用迭代的方式读文件，每次读一行
'''