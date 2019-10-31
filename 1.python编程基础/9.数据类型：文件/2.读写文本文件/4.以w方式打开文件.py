#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
以w方式打开文件时，会创建一个新文件，如果存在同名文件，原来的文件会被删除。
所有使用w方式打开文件时应该特别小心，避免删除原来有用的文件，以w方式打开文件时，只能向文件写入数据，
数据按先手顺序写入文件
'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt','w')       #以w方式打开文件
myfile.write('one\n')                                   #将字符串写入
myfile.writelines(['123','abcdefg'])                    #将列表写入
myfile.close()                                          #关闭文件
myfile=open(r'C:\Users\azhe\Desktop\123.txt','r')       #以r的方式打开文件
print(myfile.read())                                    #打印从文件中读出的数据
myfile.close()                                          #关闭文件