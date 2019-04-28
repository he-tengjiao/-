# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 11:48:07 2019

@author: Steven
"""

# 元组
a = ('a','b','c')



a = tuple()
a = ('student','teacher',12, [12,'a','c'])
a[1]
a[1] = '0'

# 元组不可变
a = tuple()
a = tuple('student')
# 索引
a[1]
# 修改会报错。
a[1] = '0'




# 字典案例
CR_7 = {'Club': '尤文图斯', 'Speed': 98, 'Finishing': 99}
print(CR_7['Club'])
print(CR_7['Speed'])

# 字典的添加（添加键值对）
CR_7['Heading'] = 95
CR_7['Nationality'] = '葡萄牙'

# 创建空字典
Messi = {}

# 修改字典值
CR_7['Speed'] = 90


# 删除键值对
del CR_7['Speed']
print(CR_7)

# 遍历键值对
for key,value in CR_7.items():
    print(key)
    print(value)



# 遍历键
for value in CR_7:
    print(value)   
    
for key in CR_7.keys():
    print(key)
    
# 遍历值
for value in CR_7.values():
    print(value)
  

# 列表嵌套字典
player = [Messi, CR_7]


# 在字典中嵌套列表
pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese'],
}





