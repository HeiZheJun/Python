#/usr/bin/python3
#-*- coding:UTF-8 -*-
'''集合中的元素是不能修改的，但是可以添加或者删除'''

'''复制集合对象'''
x ={1,3,'avv'}
y = x.copy()

'''为集合添加新元素'''
x.add('apc')

'''为集合添加多个元素'''
x.update({'npc','dse'})
print(x)

'''从集合中删除一个指定元素'''
x.remove('npc')
print(x)
x.remove('dse')
print(x)

'''从集合中删除一个随机元素'''
x.pop()
print(x)

'''删除所有元素'''
x.clear()
print(x)


'''集合使用for循环迭代'''
x = {1,2,3,'abc'}
for i in x :
    print(i)


'''集合是不可变的，不能叫可变的对象放入集合，集合、列表、字典均不能加入集合'''
'''元组可加入集合'''
x.add((1,3,4))
print(x)
