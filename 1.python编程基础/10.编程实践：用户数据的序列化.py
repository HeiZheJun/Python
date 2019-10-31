#/usr/bin/python3
#-*- coding:utf-8 -*-
'''使用文件来储存用户信息'''
import pickle
user=[]
user.append({'id':'admin','pwd':'pip123'})
user.append({'id':'test','pwd':'pip123'})
user.append({'id':'son','pwd':'pip123'})
print('代码中创建的账户信息如下')
print(user)
myfile=open(r'C:\Users\azhe\Desktop\123.txt','wb')
pickle.dump(user,myfile)
myfile.close()
myfile=open(r'C:\Users\azhe\Desktop\123.txt','rb')
x=pickle.load(myfile)
print('从文件中读出的账户信息如下：')
print(x)
