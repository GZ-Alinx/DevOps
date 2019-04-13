#!/usr/bin/python3
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from lianxi.datecheck import *
from lianxi.monitor import *

# if __name__ == '__main__':
#     m = Monitor()
#     mem = m.memory()
#     vm = m.vmstat()
#     cpu = m.cpu_info()
#     load = m.load()
#     net = m.ionetwork()
#     disk = m.disk()
#     m.com()
#     #time.sleep(10)



sv = my()

class xmail():
    def mail(self):
        my_sender = '1135189009@qq.com'  # 发件人邮箱账号
        password = 'bxrtkxzfofyygifd'  # 发件人邮箱密码
        my_user = '240579106@qq.com'  # 收件人邮箱账号，我这边发送给自己

        ret = True
        try:
            #msg = MIMEText('数据库参数如下：%s\n服务器内存：%s\nvm状态：%s' % (sv, mem, vm),  'plain', 'utf-8')
            msg = MIMEText('数据库参数如下：%s' % sv, 'plain', 'utf-8')
            msg['From'] = formataddr(["监控天神", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["背过侠", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "告警提示"  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(my_sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret = False
        return ret


ret = xmail()
Ret = ret.mail()
#while True:
#print(Ret)
def send():
    if Ret:
        return ("邮件发送成功")
    else:
        return ("邮件发送失败")
#time.sleep(5)
while True:
    Send = send()
    print(Send)
