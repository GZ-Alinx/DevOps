#传参函数

def alinx(a):
    re = print("Your Input = %s"%a)
    return re

alinx(999)

#*args 可以传入列表、元组作为参数  **kwargs 可以传入字典作为参数
d = 1
def dl(a,*args):
    kv = a + d
    print("你输入的值和 = %s"%kv)
    return kv

Sum = dl(a = int(input("Plaese input :")))
print(Sum)

