# -*- coding:utf-8 -*-

import requests
import os


def my_ip():
    ip = requests.get("http://httpbin.org/ip").json()
    IP = ip["origin"]
    return IP


IP = my_ip()


def word():
    f = open("D:\FMS\ip.txt", "a")
    Word = f.write("%s" % IP)
    f.close()
    return Word


while True:
    file = word()
    print(file)

ipchange = os.command("ping 4.4.4.4 -n 3")  # 触发换IP
try:
    if ipchange:
        while True:
            file = word()
            print(file)
except:
    print("1")
