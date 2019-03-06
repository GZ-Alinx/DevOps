import sys


for i in range(1):
    print("1")

a=0
while True:
    print('l')
    a = a+1
    if a>=2:
        break

while True:
    try:
        print("执行代码块！")
    except:
        print("执行代码块异常打印我")
    finally:
        print("warning")
    break

nested = ([1,2],[3,4],[5])

def flatten(netsted):
    for sublist in netsted:
        for el in sublist:
            yield el

sys.path.append("E:\下载\alinx.txt")