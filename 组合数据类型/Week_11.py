# -*- coding: utf-8 -*-
"""
Created on Sun May  5 10:35:21 2019

@author: Steven
"""
'''
# 4(1)
for i in range(1, 5+1):
    for j in range(1, i+1):
        print(j, end='')
    print()
    
# 4(2) while循环
n=1
while(n<6):
    i=1
    while(i<=n):
        print(str(i),end='')
        i=i+1
    print('')
    n=n+1
    
# 4(5)   
l='ABCDE' 

for i in range(len(l)):     
    for k in range(i):         
        print(end=' ')          
    print(l[i:len(l)])




# 6
a=int(input("请输入数字:"))
e = 10**(-5)
x=1
diff=1
while(diff>e):
    temp_x = x
    x=(x+a/x)/2
    diff = abs(x-temp_x)
    print(diff)


# 10
a=[34,56,78,87,88,90,101,112,520,888]
key=int(input(""))
found=False
keyi=-1
for i in range(0,len(a)):
    if a[i]==key:
        keyi=i
        found=True
        break
if not found:
    print("not found")
else:
    print("keyi=",keyi)



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


