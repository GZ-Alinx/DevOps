#多参数传递，正反向排序

def func(a, *args):
    x = list(sorted(args))
    print(x)

func(1,2,3,4,5,6,7,8,8,234,234,5,234)


def dl(d, *args):
    x = list(reversed(sorted(args)))
    print(x)

dl(1,2,3,4,5,6,7,8,8,234,234,5,234)



#匿名函数

a = lambda x:x+x  #匿名函数： 单个
print(a(15))

def func(x):
    s = x + x
    return s   #返回值
v = func(15)
print(v)


a = lambda x,y:x+y  #匿名函数: 多个
print(a(15,25))

def fun(x,y):
    s = x + y
    return s   #返回值

v = fun(15,25)
print(v)

li = [1,2,3,4,5,6,7]
d=filter(a,li)
print(d)

b = filter(lambda x:x>3,li)
print(b)
#简单函数，直接使用匿名函数定义即可。




# 函数作用域
a = 9  #全局变量
def alinx():
    a = 8   #局部变量
    k = print(a)
    return k
alinx()
print(a)
#变量名称相同，但是不在一个区域当中，作用范围也有限
#局部使用全局变量
def alin():
    global a   #全局变量不可以修改
    k = print(a)
    c = 1
    # nonlocal c  局部变量
    return k
alin()
print(a)





#闭包
def tex():
    print('tex')
tex()
tex1 = tex()
print(id(tex()))
print(id(tex1))

#函数里面定一个一个函数，并且外层函数返回李函数体
def aa():
    def bb():
        print("这是bb函数")
    print("这是aa函数")
    return bb  #返回给aa函数
    #return bb()   或者直接返回函数
aa()()




#递归和回调函数
def fun1():
    print('1')
    fun1()
#fun1()  调用就报错，无限循环调用自己

#递归就是自己来调用自己
def sum(n):
    to = 0
    for i in range(1,n+1):
        to = to + i
    return to
print(sum(100))

def fu1(z):
    if z==0:
        return 0
    return fu1(z-1)+z
print(fu1(100))


#回调
def h():
    print("888")
def h1(h,a):
    if a == 1:
        h()
    else:
        print("999")
h1(h,1)


