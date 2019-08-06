#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''print函数默认输出到标准输出流（即 sys.stdout）。
在windows命令行输出是，print函数输出到命令行窗口。
可用file参数指定输出到特定的文件'''

'''打开文件的三种模式'''
'''
r，只读模式（默认）。
w，只写模式。【不可读；不存在则创建；存在则删除内容；因为会清空原有文件的内容，一定要慎用】
a，追加模式。【可读；   不存在则创建；存在则只追加内容；】
'''
filel = open('E:\工作\汉中路/123.txt','w',encoding='utf-8')             #打开文件
print(123,'rtx2080ti',file=filel)                                       #用file指定输出到文件
filel.close()                                                           #关闭文件
print(open('E:\工作\汉中路\123.txt').read())                            #输出从文件中读出的内容

'''*.write也可以写入内容'''
#f = open('yesterday','a',encoding='utf-8')
#f.write("test1\n")