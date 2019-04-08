# 五、使用global语句修改全局变量
def spam():
    global eggs
    eggs = 'spam'
    print(eggs)

eggs = 'global'
spam()
print(eggs)



'''
# 位置实参，定义函数
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type)
    print("Its name is " + pet_name.title())

# 调用函数
describe_pet('hamster', 'Hamster harry')
describe_pet('dog', 'Dog Harry')
describe_pet('cat', 'Cat Harry')


# 关键字实参，定义函数
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type)
    print("its name is " + pet_name.title())

# 调用函数
describe_pet(pet_name='Harry',animal_type='hamster')



# 默认值实参，定义函数
def describe_pet(animal_type, pet_name='Tom'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type)
    print("its name is " + pet_name.title())

# 调用函数
describe_pet(animal_type='Dog')
#describe_pet('Cat')


# 任意数量实参，定义函数
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
    
# 调用函数
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


###################################
# 函数作用域
def f1():
    a = 1
    b = 1

f1()
print(a)

# 二、局部作用域不能使用其他局部作用域内的变量

def f1():
    a = 99
    f2()
    print(a)

def f2():
    b = 1
    a = 2

f1()

# 三、全局变量可以在局部作用域中读取
def f1():
    print(a)

a = 3
f1()
print(a)


# 四、名称相同的局部变量和全局变量
def spam():
    eggs = 'spam local'
    print(eggs) 
def bacon():
    eggs = 'bacon local'
    print(eggs) 
    spam()
    print(eggs)


def f1():
    print(eggs)

eggs = 'global'
bacon()
print(eggs)
f1()


# 五、使用global语句修改全局变量
def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)



# 鸡兔同笼代码
def calculate(n_heads,n_legs):
    check = 0
    for n_chicks in range(0,n_heads+1):
        n_rabbits = n_heads - n_chicks
        total_legs = 4*n_rabbits+2*n_chicks
        if total_legs==n_legs:
            print("鸡和兔的个数分别为：", n_chicks, n_rabbits)
            check = 1
            
    if check == 0:
        print("不存在")
        
legs=int(input("输入腿的个数："))
heads=int(input("输入头的个数："))
calculate(heads, legs)



# 蜘蛛，鸡，兔同笼问题：一个农场主，同时养了蜘蛛，鸡和兔。输入头和腿的个数，使用穷举法，计算出蜘蛛，鸡与兔所有可能的组合情况。如果不存在组合情况，则返回“不存在”，代码如下：


def calculate(n_heads,n_legs):
    i=0#初始化的计数器
    for n_chicks in range(0,n_heads+1):
        for n_rabbits in range(0, n_heads+1):
            n_spider=n_heads-n_chicks-n_rabbits
            total_legs=8*n_spider+4*n_rabbits+2*n_chicks
            if total_legs==n_legs:
                i=i+1
                print("第"+str(i)+"种可能组合")
    if i==0:
        print("组合不存在")
        return None
    else:
        return None
            
def solve():
    legs=int(input("输入腿的个数："))
    heads=int(input("输入头的个数："))
    calculate(heads,legs)

solve()


'''

