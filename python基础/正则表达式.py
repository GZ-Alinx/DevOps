import re

"""re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

re.match(pattern, string, flags=0)

函数参数说明：
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""

print(re.match('www', 'www.alinx.top').span())
print(re.match('top', 'www.alinx.top'))


#实例


line = "I love you My god"
mathobj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
print(mathobj)
if mathobj:
    print "matchobj()", % mathobj.group()



# re.search方法

re.search()
re.search(pattern, string, flags=0)
"""
函数参数说明：

参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。
"""

