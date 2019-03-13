
# python数据库操作
# python -m pip install mysql-connector


import mysql.connector

#创建数据库连接

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    database="runoob"
)

print(mydb)
mydb.close()


#创建数据库

mydbs = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
)

#我们要使用连接对象获得一个cursor对象,接下来,我们会使用cursor提供的方法来进行工作. 这些方法包括两大类:1.执行命令,2.接收返回值
mysursor = mydbs.cursor()
#mysursor.execute("CREATE DATABASE LX")   #执行创建数据库语句
mydbs.close()                            #关闭数据库

#  cursor用来执行命令的方法:
# 　 callproc(self, procname, args):          用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
# 　 execute(self, query, args):              执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# 　 executemany(self, query, args):          执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
# 　 nextset(self):                           移动到下一个结果集
#
# 　 cursor用来接收返回值的方法:
# 　 fetchall(self):                          接收全部的返回结果行.
# 　 fetchmany(self, size=None):              接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# 　 fetchone(self):                          返回一条结果行.
# 　 scroll(self, value, mode='relative'):    移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,如果mode='absolute',则表示从结果集的第一 行移动value条.




#输出存在的数据库
myds = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    #database="lx"
)

db = myds.cursor()
db.execute("show databases")

for x in db:
    print(x)
print("以上是数据库信息")

#直接指定数据库连接，如果不存在则报错

lxdb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    database="lx"
)

#创建数据库表
tabs = lxdb.cursor()
#tabs.execute("create table dl (name VARCHAR(255), url VARCHAR(255))")

#查看数据表是否存在
tabs.execute("show tables")
for x in tabs:
    print(x)


# 给表添加主键

# tabs.execute("ALERT TABLE dl ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# tabs.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



# 插入数据

sql = "INSERT INTO alinx (name, url) VALUES (%s, %s)"
val = ("lx", "http://www.alinx.top")  #不支持中文
tabs.execute(sql, val)

lxdb.commit()  #数据更新必须使用该语句
print(tabs.rowcount, "数据插入成功")

lxdb.close()

####################

dldb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    database="lx"
)

ld = dldb.cursor()

#批量插入
sql = "INSERT INTO alinx (name, url) VALUSE (%s, %s)"

val = [
    ('dl', 'www.dongli.com'),
    ('lj', 'www.lijie.com'),
    ('taobao', 'www.taobao.com'),
    ('csdn', 'blog.csdn.net/')
]

ld.executemany(sql, val)

lxdb.commit()

print(tabs.rowcount, "数据插入成功")


