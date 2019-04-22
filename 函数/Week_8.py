#e8.1DrawKoch.py
import turtle
def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
           turtle.left(angle)
           koch(size/3, n-1) 
def main():
turtle.setup(800,400)
turtle.speed(0)  #控制绘制速度
    turtle.penup()
    turtle.goto(-300, -50)
    turtle.pendown()
    turtle.pensize(2)
    koch(600,3)     # 0阶科赫曲线长度，阶数
    turtle.hideturtle()
main()


'''
#e7.1DrawSevenSegDisplay.py
import turtle, datetime
def drawLine(draw):   #绘制单段数码管
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)
def drawDigit(d): #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,6,8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20) 
def drawDate(date):  #获得要输出的数字
    for i in date:
        drawDigit(eval(i))  #注意: 通过eval()函数将数字变为整数
def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.hideturtle()
main()





# datetime案例
from datetime import datetime
print(datetime.utcnow())




# 递归案例
def reverse(s):
    if s == '':
        return s
    else:
        return reverse(s[1:]) + s[0]

print(reverse('ABCDEFGH'))




# 蜘蛛，鸡，兔同笼问题：一个农场主，同时养了蜘蛛，鸡和兔。输入头和腿的个数，使用穷举法，计算出蜘蛛，鸡与兔所有可能的组合情况。如果不存在组合情况，则返回“不存在”，代码如下：

def calculate(n_heads,n_legs):
    i=0#初始化的计数器
    for n_chicks in range(0,n_heads+1):
        for n_rabbits in range(0, n_heads+1):
            n_spider=n_heads-n_chicks-n_rabbits
            total_legs=8*n_spider+4*n_rabbits+2*n_chicks
            if (total_legs==n_legs) and (n_spider>=0):
                i=i+1
                print("第"+str(i)+"种可能组合:","鸡：",n_chicks,"兔子：",n_rabbits, "蜘蛛：", n_spider)
    if i==0:
        print("组合不存在")
            

legs=int(input("输入腿的个数："))
heads=int(input("输入头的个数："))
calculate(heads,legs)
'''
