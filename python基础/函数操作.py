
# page = download_page()
# freqs = compute_frequencies(page)
# for word, freq in freqs:
#     print(word, freq)


def alinx(num):
    result = [0,1]
    for i in range(num -2):
        result.append(result[-2])
    return result
print(alinx(15))

def test():
    print('This is good')
    return
    print('This is not')

test()

#字符串格式化
gs = str('alin')
print('gs = %s' % gs)
#'%s %s'%(str1,str2)   多个值拼接
# %d  数字
# %f  浮点数
# %c  ASCLL字符
# %o  8进制
# %x  16进制
# %e  科学计数法

#字符串拼接
po = '1'.join(['a','b','c'])
print('po %s'% po)

#format方法
aa = '{}'.format('alinx')
aa = '{}{}{}'.format('alinx',123,321)
print('aa=%s'%aa)

aa = '{2}{0}{1}'.format('拼接','format','下标')
print(aa)

aa = '{a}{b}{c}'.format(a='alinx',b='haha',c='xixi')
print(aa)

#左对齐输出
a = '{a:<10}'.format(a=123)
#右对齐
a = '{a:>10}'.format(a=123)
print(a)
#*号补齐空位
a = '{a:*>10}'.format(a=123)
print(a)
#剧中对齐
a = '{a:^10}'.format(a=123)
print(a)

a = '{{hello{}}}'.format('alinx')
print(a)

#深浅复制
import copy

li = 1
li1 = li
li2 = copy.copy(li)
print(id(li))
print(id(li2))
#id值相同
#深复制 赋值过去
li3 = copy.deepcopy(li)
print(id(li3))


#函数操作
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

ali = {}
init(ali)
print(ali)


#获取人员姓名
def lookup(data, label, name):
    return data[label].get(name)

print(dir(__builtins__))  #查看内置函数

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = 'first', 'middle', 'last'

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


# 函数store执行如下步骤。
# (1) 将参数data和full_name提供给这个函数。这些参数被设置为从外部获得的值。
# (2) 通过拆分full_name创建一个名为names的列表。
# (3) 如果names的长度为2（只有名字和姓），就将中间名设置为空字符串。
# (4) 将'first'、'middle'和'last'存储在元组labels中（也可使用列表，这里使用元组只是为了省略方括号）。
# (5) 使用函数zip将标签和对应的名字合并，以便对每个标签名字对执行如下操作：
#  获取属于该标签和名字的列表；
#  将full_name附加到该列表末尾或插入一个新列表。





#异常处理

while True:
    try:
        y = int(input('Please input sum:'))
        x = int(input('Please input V:'))
        print( y / x )
    except ZeroDivisionError:
        print("The Action Error!")
    except TypeError:
        print("The Type Error!")
    except ValueError:
        print("V Error~!")
    except (ZeroDivisionError, TypeError, ValueError):  #元组中指定多个代替多句
        print("Please input Success~")
    #打印异常继续执行
    except (ZeroDivisionError,TypeError,ValueError) as e:
        print(e)
    except:
        print("异常了")
    # 像这样捕获所有的异常很危险，因为这不仅会隐藏你有心理准备的错误，还会隐藏你没有考虑过的错误。
    # 这还将捕获用户使用Ctrl + C终止执行的企图、调用函数sys.exit来终止执行的企图等。在大多数情
    # 况下，更好的选择是使用except Exception as e并对异常对象进行检查。这样做将让不是从Exception
    # 派生而来的为数不多的异常成为漏网之鱼，其中包括SystemExit和
    # KeyboardInterrupt，因为它们是从BaseException（Exception的超类）派生而来的。
    else:
        break
    finally:
        print("finally 如果try中的异常没有在exception中被指出，那么系统将会抛出Traceback(默认错误代码）,并且终止程序，接下来的所有代码都不会被执行，但如果有Finally关键字，则会在程序抛出Traceback之前（程序最后一口气的时候），执行finally中的语句。这个方法在某些必须要结束的操作中颇为有用，如释放文件句柄，或释放内存空间等")

#指定异常如果没有被匹配，将会执行finnally代码块  不管程序有没有异常，finally中的语句必会执行。






class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

calcc = MuffledCalculator()
sd = calcc.calc('10 / 2')
print(sd)