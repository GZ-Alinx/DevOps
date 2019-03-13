import time
import datetime
import random
import sys
import os
import json
import re
import logging

print(random.random())

#随机选择一个数
print(random.choice([1,2,3,4,5,6,67,8,9,12,5,3,63,486,678,5,3,2,564]))

#随机选择两个数
#print(random.sample(int[1, 2, 3, 5, 67]))

#随机生成验证码
def keys():
    ret = ""
    for i in range(6):
        num = random.randint(0,9)
        alf = chr(random.randint(65,122))
        num_s = str(random.choice([num,alf]))
        ret +=num_s
    return ret

print(keys())

t = time.localtime()
print(t)


s = datetime.datetime.now()
print(s)

#打印本身路径
print(sys.argv)
print(sys.version)
print(sys.path)


os模块
os.getcwd() #获取当前工作目录，即当前python脚本工作的目录路径
os.chdir("dirname")  #改变当前脚本工作目录；相当于shell下cd
os.curdir  #返回当前目录: ('.')
os.pardir  #获取当前目录的父目录字符串名：('..')
os.makedirs('dirname1/dirname2')    #可生成多层递归目录
os.removedirs('dirname1')    #若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir('dirname')    #生成单级目录；相当于shell中mkdir dirname
os.rmdir('dirname')    #删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
os.listdir('dirname')    #列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
os.remove()  #删除一个文件
os.rename("oldname","newname")  #重命名文件/目录
os.stat('path/filename')  #获取文件/目录信息
os.sep    #输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
os.linesep    #输出当前平台使用的行终止符，win下为"\t\n",Linux下为"\n"
os.pathsep    #输出用于分割文件路径的字符串 win下为;,Linux下为:
os.name    #输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system("bash command")  #运行shell命令，直接显示
os.environ  #获取系统环境变量
os.path.abspath(path)  #返回path规范化的绝对路径
os.path.split(path)  #将path分割成目录和文件名二元组返回
os.path.dirname(path)  #返回path的目录。其实就是os.path.split(path)的第一个元素
os.path.basename(path) # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
os.path.exists(path)  #如果path存在，返回True；如果path不存在，返回False
os.path.isabs(path)  #如果path是绝对路径，返回True
os.path.isfile(path)  #如果path是一个存在的文件，返回True。否则返回False
os.path.isdir(path)  #如果path是一个存在的目录，则返回True。否则返回False
os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
os.path.getatime(path)  #返回path所指向的文件或者目录的最后存取时间
os.path.getmtime(path)  #返回path所指向的文件或者目录的最后修改时间



x="[null,trye,false,1]"
print(json.loads(x))


#re 正则模块
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='C:\log',
                    filemode='w')
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

