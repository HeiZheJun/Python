#/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == '__main__':
    #模块独立运行时，执行下面代码
    def show():
        print('test7独立运行')
    show()
    import sys
    print(sys.argv)
else:
    #作为导入模块时，执行下面的代码
    def show():
        print('test7作为导入模块')
print('test7执行完毕')
