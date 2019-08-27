#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''bytes对象是一个不可变的字节对象序列，是一种特殊字符串
可称为bytes字符串。bytes字符串用前缀b和传统的字符串表示'''
'''例如单引号：b'a' b'b' b'123' b'acb'
双引号：b"a" b"123" b"abc"
三单引号或三双引号：b"""123""" 
'''
'''在bytes字符串中只能包含ASCII码字符'''
x = b"abc"
print(x)
print(type(x))
'''bytes字符串支持前面各种字符串操作，不同之处在于使用索引时返回的是字符串对应的ASCII码'''
print(x[0])
'''可用十六进制显示bytes字符串
'''
print(x.hex())
