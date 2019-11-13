#/usr/bin/python3
#-*- coding:utf-8 -*-
'''
    在作为导入模块使用时，模块__name__属性值为模块文件的主名。当作为顶层模块直接执行时，__name__属性值为“__main__”。
    在下面的test7中检查__name__属性值是否为__main__。如果为__main__则将命令行参数输出
'''
import test7
test7.show()
'''
    通过检查__name__属性是否为__main__,可以分别定义作为顶层模块或导入模块执行时的代码
'''