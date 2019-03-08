a, b, c, *ss, ds = 1,2,3,4,5,6,7,8,9
print(*ss)

x = y = ss
print(x)

name = input('plaese input:')
if name.endswith('5'):
    print('猜对了')
elif name.endswith('6'):
    print("很厉害哦")
else:
    print('你猜错了')


status = "yyy" if name.endswith("alinx") else "stranger"
print(status)

x = 5,6,7
y = 6,7
c = x is not y
print(c)

b = x is not y # is 相反
print(b)


# while True:
#     print('888')

alinx = 1
while alinx <= 100:
    print(alinx)
    alinx += 1

name = ''
while not name:
    name = input('Please Enter Name:')
print('Hello, {}!'.format(name))
#
# while True:
#     print('666')

alinx = ['500','alinx','lijie']
for alinx in alinx:
    print('遍历数组')

list = list(range(0, 10))

for list in list:
    print('k')

#遍历字典
d = {'s':1,'d':2,'g':3}
for key in d:
    print(key, 'corresponds to', d[key])


#并行迭代
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]

for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')
#i是用作循环索引的变量的标准名称。一个很有用的并行迭代工具是内置函数zip，它将两个
#序列“缝合”起来，并返回一个由元组组成的序列。返回值是一个适合迭代的对象，要查看其内
#容，可使用list将其转换为列表。
dd = list(zip(name, ages))
print(dd)


#1. exec
#函数exec将字符串作为代码执行。
nn = exec("print('Hello, world!')")
print(nn)
