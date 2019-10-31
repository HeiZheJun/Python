#/usr/bin/python3
#-*- coding:utf-8 -*-
'''a+与a方式的区别是前者除了允许写入数据，还可以读出数据'''
myfile=open(r'C:\Users\azhe\Desktop\123.txt','a+')      #以a+方式打开文件
print(myfile.tell())                                    #返回指针位置
myfile.write('\nyang is my son')                        #将字符串写入文件
myfile.seek(0)
print(myfile.read())                                    #打印读出的内容，可以看到写入的字符串在末尾
myfile.close()


