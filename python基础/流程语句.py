# while 循环
s = 1
while s == 1:
    print("s = %s"%s)
    break


# for 循环
for i in range(1,10):
    print(i)

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

# if 条件控制
a = 1
if a == 1:
    print("a = %s"%a)
elif a == 2:
    print("a = %s"%a)
else:
    print("a = %s"%a)


