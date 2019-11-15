#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''
    class语句执行，类对象即被创建， 便可进一步使用类对象来访问类的属性、创建实例对象
'''
class   testclass:
    data = 100
    def setpdata(self,value):
        self.data=value
    def showdata(self):
        print('self.data=',self.data)
    print('类testclass加载成功')
print(type(testclass))                  #测试类对象的类型，python中所有类对象都是type类型