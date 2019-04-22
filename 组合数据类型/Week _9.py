# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:27:05 2019

@author: Steven
"""

# 列表添加.append()
Name = []
Name.append("小明")
Name.append("小红")
Name.append("小蓝")
print(Name)

# 列表添加.insert()
Name.insert(1, "大明")
print(Name)


# 列表修改
Name[1] = "老明"
print(Name)

# 列表删除 del语句
del Name[1]


# 列表删除 pop()方法
temp = Name.pop()
print(Name)

# # 列表删除 remove()方法
Name.remove("小明")
print(Name)



# 列表作用域

# 列表的复制1
a = ['A', 'B', 'C']
b = a
b[1] = 'W'
print(a)
print(b)

print(id(a))
print(id(b))


# 列表的复制2
a = ['A', 'B', 'C']
b = ['A', 'B', 'C']
b[1] = 'W'
print(a)
print(b)
print(id(a))
print(id(b))

# 列表的复制3
a = ['A', 'B', 'C']
b = a[:]
b[1] = 'W'
print(a)
print(b)

print(id(a))
print(id(b))



# 列表的复制4
a = ['A', 'B', 'C']
b = a.copy()
b[1] = 'W'
print(a)
print(b)
print(id(a))
print(id(b))


# 列表的作用域
def f():
    a[1] = "W"
    print(id(a))

a = ['A', 'B', 'C']
print(id(a))
f()
print(a)
print(id(a))



# 元组
a = ('a','b','c')

# 元组不可变
a = tuple()

a = tuple('student')
# 索引
a[1]

# 修改会报错。
a[1] = '0'





