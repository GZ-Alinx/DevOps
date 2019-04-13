#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pymysql
import time


db = pymysql.connect(
    host = "",
    user = "",
    passwd = "",
    db = "mysql"
)

sqlcmd = db.cursor()

def my():
    a = sqlcmd.execute("SHOW STATUS LIKE '%Connections%'")
    return ("数据库访问量：%s" % a)  #模块调用直接返回，不需要做啥！


while True:
    ss=my()
    time.sleep(1)
    break