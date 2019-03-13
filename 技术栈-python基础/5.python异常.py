
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



import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise