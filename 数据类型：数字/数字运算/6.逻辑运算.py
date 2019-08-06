#/usr/bin/python3
# -*- coding:UTF-8 -*-
'''逻辑运算（布尔运算)指逻辑值（True或False）执行not、and或or操作'''
'''在判断逻辑值时，属于下列情况的值python都视为假逻辑'''
'''None'''
'''False'''
'''各种数字类型的0、如0 0.0 （0+0j）'''
'''空的序列 " "、（）、[]'''
'''空的映射{}'''
'''包含了返回值为0或者false的_bool_()或_len_()方法的用户自定义类的实例'''
'''上述情况只为的值视为逻辑真'''

'''逻辑非not'''
print(not True,not False)
print(not None,not 0, not '',not{})

'''逻辑与and'''
'''x and y 在这两个操作都为True时结果才为True，否则为False，当x为False时，and的运算结果肯定为False
python不会再计算y'''
print(True and True,True and False,False and False,False and True)

'''逻辑或or'''
'''x or y 在两个操作数都为False是，结果才为False，否则为True
当x为True是 or的结果肯定是True，python不会再计算y'''
print(True or True,True or False,False or True,False or False)

