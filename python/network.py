# -*- coding:utf-8 -*-

import psutil
import time



def get_key():
    key_info = psutil.net_io_counters(pernic=True).keys() # 获取网卡名称
    recv = {}
    sent = {}

    for key in key_info:
        recv.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_recv)   # 各网卡接收的字节数
        sent.setdefault(key, psutil.net_io_counters(pernic=True).get(key).bytes_sent)   # 各网卡发送的字节数

    return key_info, recv, sent


def get_rate(func):
    key_info, old_recv, old_sent = func()  # 上一秒收集的数据
    time.sleep(1)
    key_info, now_recv, now_sent = func()  # 当前所收集的数据

    net_in = {}
    net_out = {}

    for key in key_info:
        net_in.setdefault(key, (now_recv.get(key) - old_recv.get(key)) / 1024)  # 每秒接收速率
        net_out.setdefault(key, (now_sent.get(key) - old_sent.get(key)) / 1024)  # 每秒发送速率

    return key_info, net_in, net_out


input1 = 0
output1 = 0
while 1:
    try:
        key_info, net_in, net_out = get_rate(get_key)
        for key in key_info:
            #print('%s\nInput:\t %-5sKB/s\nOutput:\t %-5sKB/s\n' % (key, net_in.get(key), net_out.get(key)))
            input1 += net_in.get(key)
            output1 += net_out.get(key)
            #os.system('cls')
    except KeyboardInterrupt:
        exit()
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("北京时间：%s" % now)
    print("总下载流量: %s" % input1)
    print("总上传流量: %s" % input1)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")