#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
import和from语句在执行导入操作时，会执行被导入的模块。模块中的赋值语句执行时创建变量，def语句执行时创建函数对象。
总之，模块中的全部语句都会被执行，而且只执行一次。当再次使用import或者from语句导入模块时，并不会执行模块代码
而只是重新建立到已经创建的对象引用而已

所以import和from语句是隐性的赋值语句
    ·python执行import语句时，创建一个模块对象和一个与模块文件同名的变量，并建立变量和模块对象的引用
    ·python执行from语句时，会同时在当前模块和导入模块中创建同名变量，病因通模块在执行时创建的对象
'''
'''下面的模块文件test.py包含了一条赋值语句、一个函数定义和一条输出语句'''
'''x = 100                                                 #赋值、创建变量x
def show():
    print('这是模块test.py中的show()函数中的输出！')
print('这是模块test.py中的show()函数中的输出！')'''
'''下面通过使用该模块说明导入操作'''
import test     #导入模块，输出说明在模块被导入时执行
print(test.x)   #使用模块变量
test.x = 200    #为模块变量赋值
import test     #重新导入模块
print(test.x)   #使用模块变量，输出结果显示重新导入未影响变量的值
print(test.show())  #调用模块的函数
abc = test      #将模块变量赋值给另一个变量
print(abc.x)    #使用模块变量
print(abc.show())   #调用模块函数

'''
在上面的代码执行过程和输出结果可以看出，重新导入并不会改变模块中变量在之前已经赋的值，
在执行了import test后，test是与模块文件同名的变量，所以可以将它赋值给另一个变量abc，引用同一个模块对象
'''

'''
在考察使用from导入test模块
'''
#这里值显示200的原因是上面import导入造成的，重新创个新文件进行测试好了
from test import x,show     #导入模块中的变量名想，show
print(x)                    #输出模块中变量的原始值
show()                      #调用函数模块
x =200                      #为当前模块变量赋值
from test import x,show     #重新导入
print(x)                    #x的值为模块中变量的原始值

'''
在执行from语句时，可以看到模块中的所有语句被执行，显示了输出结果。from语句将模块中的变量x和show赋值给当前模块中的变量名x
和show。语句‘x=200’只是为了当前模块中的变量x赋值，不会影响到模块中的变量x。再重新导入后，当前模块变量x被重新赋值为test
模块变量x的值
'''
'''从对比可以看出，import导入模块后，可使用模块变量名‘test’作为限定词，直接使用模块中的变量和函数；而from通过将模块的
变量赋值给当前模块中的同名变量，来引用当前模块中的变量'''