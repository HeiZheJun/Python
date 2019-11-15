#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''类定义的格式如下：
    class   类名：
        赋值语句
        赋值语句
        ……
        def语句定义函数
        def语句定义函数
各种语句的先后顺序没有关系
'''
class   testclass:
    data = 100
    def setpdata(self,value):
        self.data=value
    def showdata(self):
        print('self.data=',self.data)
    print('类testclass加载成功')
if __name__ == '__main__':
    testclass.setpdata(testclass,200)
    testclass.showdata(testclass)


