#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
如果直接用文本文件或者二进制文件格式存储python的各种对象，通常需要进行繁琐的转换
可以用python的标准模板pickle处理文件中对象的读写
'''
import pickle
x=[1,2,'abc']
y={'name':'zhemei','age':22}
myfile=open(r'C:\Users\azhe\Desktop\123.txt','wb')
pickle.dump(x,myfile)                                   #将列表对象导入到文件
pickle.dump(y,myfile)
myfile.close()
myfile=open(r'C:\Users\azhe\Desktop\123.txt','rb')
print(myfile.read())                                    #读出文件中的全部内容
myfile.seek(0)
print(pickle.load(myfile))                              #打印文件内容
print(pickle.load(myfile))                              #打印文件内容
x=pickle.load(myfile)                                   #存储文件内容
y=pickle.load(myfile)                                   #存储文件内容