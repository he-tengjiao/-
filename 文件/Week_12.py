# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:35:21 2019

@author: Steven
"""

'''
# 文本文件与二进制文件的区别
textFile = open("7.1.txt","rt") #t表示文本文件方式
print(textFile.readline())
textFile.close()
binFile = open("7.1.txt","rb")   #r表示二进制文件方式
print(binFile.readline())
binFile.close()



# 读取整个文件
File = open('D:\\Hello.txt')
#读取整个文件
File.read()
# 读取一行一行
File.readlines()
File.close()

# 写文本
File = open('D:\\Hello.txt','w')
File.write('锄禾日当午\n')
File.close()
File = open('D:\\Hello.txt','a')
File.write('Python\n')
File.close()
'''

'''
# 读取整个文件，绝对路径和相对路径
File1 = open('D:\\Hello.txt')
File2 = open('Hello.txt')
#读取整个文件
File1.read()
File2.read()
# 读取一行一行
File1.readlines()
File1.close()
File2.readlines()
File2.close()


# 进行文本逐行打印：
fo = open('hello.txt','r')
for line in fo.readlines():
    print(line)
fo.close()

# 打开文件
fo = open('诛仙.txt','r', encoding='utf-8')
for line in fo:
    print(line)
fo.close()




# 文件写入——覆盖写模式
fo = open('bacon.txt','w')
fo.write('ABCDEF\n')
fo.close()


# 文件写入——追加写模式
fo = open('bacon.txt','a')
fo.write('ABCDEF\n')
fo.close()


# 案例：向文件写入列表
fo = open('new_bacon.txt','w+')
ls = ['唐诗','宋词','元曲']
fo.writelines(ls)
fo.seek(0)
for line in fo:
    print(line)
fo.close()


# with语句打开文件
with open('new_bacon.txt', 'r') as f:
    print(f.read())
'''

# 打开一个图片，在解释器中使用
from PIL import Image
im = Image.open("D:\\marvel.jpg")
print(im.format, im.size, im.mode)

