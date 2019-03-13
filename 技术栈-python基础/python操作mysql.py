"""
什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
"""

import pymysql
import mysql.connector

#
# # #打开数据库
# lx = pymysql.connect("localhost", "root", "gslixiong", "mysql")
# # 使用cursor（） 方法创建一个游标对象 cursor
# cursor = lx.cursor()
# # 使用execute() 方法执行sql查询
# cursor.execute("select version()")
# # 使用 fetchone() 方法获取单条数据
# data = cursor.fetchone()
# print ("Database version : %s " % data)
# # #关闭数据库连接
# lx.close()



#数据库连接 不存在则报错
# dbs = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="gslixiong",
#     database="runoob"
# )
# print(dbs)
#
# #创建数据库、表
# mycursor = dbs.cursor()
# mycursor.execute("CREATE TABLE site (name VARCHAR(255), url VARCHAR(255))")  #只能执行一条，多条则报错
# for x in mycursor:
#     print(x)
#
# dbs.close()



#插入数据

Dbs = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    database="runoob"
)

mycursor = Dbs.cursor()
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/')
]

mycursor.executemany(sql, val)
Dbs.commit()  # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")



#数据查询
medb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="gslixiong",
    database="runoob"

)

mycu = medb.cursor()
mycu.execute("select * from sites")
meresult = mycu.fetchall()

#for x in myr