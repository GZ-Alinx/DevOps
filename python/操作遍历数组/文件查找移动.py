import os


# 遍历文件内容并操作

file = open("/root/ip.txt", "r")
url = ("/root")
durl = ("/root/pages/")
while True:
    line = file.readlines()
    os.system("find %s -name %s |xargs -I {} mv {} %s " % (url, line, durl))

    if not line:
        break



