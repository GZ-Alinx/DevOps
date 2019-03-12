"""
什么是 PyMySQL？
PyMySQL 是在 Python3.x 版本中用于连接 MySQL 服务器的一个库，Python2中则使用mysqldb。

PyMySQL 遵循 Python 数据库 API v2.0 规范，并包含了 pure-Python MySQL 客户端库。
"""

import pymysql

# #打开数据库
lx = pymysql.connect("localhost", "root", "gslixiong", "mysql")
# 使用cursor（） 方法创建一个游标对象 cursor
cursor = lx.cursor()
# 使用execute() 方法执行sql查询
cursor.execute("select version()")
# 使用 fetchone() 方法获取单条数据
data = cursor.fetchone()
print ("Database version : %s " % data)
# #关闭数据库连接
db.close()


#数据插入
dbs = pymysql.connect