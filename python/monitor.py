#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'liao gao xiang'

import re
import time
from datetime import datetime
import pexpect


class Monitor(object):
    """服务器自动化监控"""

    def __init__(self):
        self.host = "218.17.119.242"
        self.user = "root"
        self.password = "iet6Iih0shei3quakohzaec2"

    def ssh_command(self, command):
        """SSH登录执行命令"""
        ssh = pexpect.spawn('ssh -l {} {} {}'.format(self.user, self.host, command))  # 登录口令
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=30)
        if i == 0:
            ssh.sendline(self.password)
        if i == 1:
            ssh.sendline('yes')
            ssh.expect('[p,P]assword: ')
            ssh.sendline(self.password)
        index = ssh.expect(["$", "#", pexpect.EOF, pexpect.TIMEOUT])  # 此处注意，root用户登录符号为#，普通用户为$
        if index != 0:
            print("登录失败！报错内容：{}；{}".format(ssh.before.decode("utf-8"), ssh.after.decode("utf-8")))
            return False
        return ssh

    def memory(self):
        """内存监控"""
        ssh = self.ssh_command("cat /proc/meminfo")
        ssh.expect(pexpect.EOF)
        data = re.findall(r"(\d+) kB", ssh.before.decode("utf-8"))  # ssh.before结果为bytes类型，使用utf-8解码为string
        MemTotal = int(data[0]) // 1024  # 除以1024得到MB
        MemFree = int(data[1]) // 1024
        Buffers = int(data[2]) // 1024
        Cached = int(data[3]) // 1024
        SwapCached = int(data[4]) // 1024
        SwapTotal = int(data[13]) // 1024
        SwapFree = int(data[14]) // 1024
        print("*******************内存监控 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("总内存: {} MB".format(MemTotal))
        print("空闲内存: {} MB".format(MemFree))
        print("给文件的缓冲大小: {} MB".format(Buffers))
        print("高速缓冲存储器使用的大小: {} MB".format(Cached))
        print("被高速缓冲存储用的交换空间大小: {} MB".format(SwapCached))
        print("给文件的缓冲大小: {} MB".format(Buffers))
        if int(SwapTotal) == 0:
            print("交换内存总共为：0")
        else:
            print("交换内存利用率: {}%".format(round((SwapTotal - SwapFree) / float(SwapTotal) * 100, 2)))
        print("内存利用率: {}%".format(round((MemTotal - MemFree) / float(MemTotal) * 100, 2)))

    def vmstat(self):
        """内核线程、虚拟内存、磁盘和CPU活动的统计信息"""
        ssh = self.ssh_command("vmstat 1 2 | tail -n 1")
        ssh.expect(pexpect.EOF)
        vmstat_info = ssh.before.decode("utf-8").strip().split()
        processes_waiting = vmstat_info[0]
        processes_sleep = vmstat_info[1]
        swpd = int(vmstat_info[2]) // 1024
        free = int(vmstat_info[3]) // 1024
        buff = int(vmstat_info[4]) // 1024
        cache = int(vmstat_info[5]) // 1024
        si = int(vmstat_info[6]) // 1024
        so = int(vmstat_info[7]) // 1024
        io_bi = vmstat_info[8]
        io_bo = vmstat_info[9]
        system_interrupt = vmstat_info[10]
        system_context_switch = vmstat_info[11]
        cpu_user = vmstat_info[12]
        cpu_sys = vmstat_info[13]
        cpu_idle = vmstat_info[14]
        cpu_wait = vmstat_info[15]
        st = vmstat_info[16]
        print("*******************vmstat信息统计 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("等待运行进程的数量: {}".format(processes_waiting))
        print("处于不间断状态的进程: {}".format(processes_sleep))
        print("使用虚拟内存(swap)的总量: {} MB".format(swpd))
        print("空闲的内存总量: {} MB".format(free))
        print("用作缓冲的内存总量: {} MB".format(buff))
        print("用作缓存的内存总量: {} MB".format(cache))
        print("交换出内存总量 : {} MB".format(si))
        print("交换入内存总量 : {} MB".format(so))
        print("从一个块设备接收: {}".format(io_bi))
        print("发送到块设备: {}".format(io_bo))
        print("每秒的中断数: {}".format(system_interrupt))
        print("每秒的上下文切换数: {}".format(system_context_switch))
        print("用户空间上进程运行的时间百分比: {}".format(cpu_user))
        print("内核空间上进程运行的时间百分比: {}".format(cpu_sys))
        print("闲置时间百分比: {}".format(cpu_idle))
        print("等待IO的时间百分比: {}".format(cpu_wait))
        print("从虚拟机偷取的时间百分比: {}".format(st))

    def cpu_info(self):
        """CPU信息获取"""
        ssh = self.ssh_command("cat /proc/cpuinfo")
        ssh.expect(pexpect.EOF)
        cpu_num = re.findall(r"processor.*?(\d+)", ssh.before.decode("utf-8"))[-1]
        print("*******************CPU信息 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("CPU数目: {}".format(str(int(cpu_num) + 1)))
        li = ssh.before.decode("utf-8").replace('\t', '').split('\r')
        CPUinfo, procinfo, nprocs = {}, {}, 0
        for line in li:
            if line.find("processor") > -1:
                CPUinfo['CPU%s' % nprocs] = procinfo
                nprocs = nprocs + 1
            else:
                if len(line.split(':')) == 2:
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
        for processor in CPUinfo.keys():
            print("CPU属于的名字及其编号、标称主频: {}".format(CPUinfo[processor]['model name']))
            print("CPU属于其系列中的哪一代的代号: {}".format(CPUinfo[processor]['model']))
            print("CPU制造商: {}".format(CPUinfo[processor]['vendor_id']))
            print("CPU产品系列代号: {}".format(CPUinfo[processor]['cpu family']))
            print("CPU的实际使用主频: {} GHz".format(round(float(CPUinfo[processor]['cpu MHz']) / 1024, 2)))

    def load(self):
        """监控负载"""
        ssh = self.ssh_command("cat /proc/loadavg")
        ssh.expect(pexpect.EOF)
        loadavg = ssh.before.decode("utf-8").strip().split()
        print("*******************负载均衡监控 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print("系统5分钟前的平均负载: {}".format(loadavg[0]))
        print("系统10分钟前的平均负载: {}".format(loadavg[1]))
        print("系统15分钟前的平均负载: {}".format(loadavg[2]))
        print("分子是正在运行的进程数,分母为总进程数: {}".format(loadavg[3]))
        print("最近运行的进程ID: {}".format(loadavg[4]))

    def ionetwork(self):
        """获取网络接口的输入和输出"""
        ssh = self.ssh_command("cat /proc/net/dev")
        ssh.expect(pexpect.EOF)
        li = ssh.before.decode("utf-8").strip().split('\n')
        print("*******************网络接口的输入和输出监控 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        net = {}
        for line in li[2:]:
            net_io = {}
            line = line.split(":")
            eth_name = line[0].strip()
            net_io['Receive'] = round(float(line[1].split()[0]) / (1024.0 * 1024.0), 2)  # bytes / 1024 / 1024 得到MB
            net_io['Transmit'] = round(float(line[1].split()[8]) / (1024.0 * 1024.0), 2)
            net[eth_name] = net_io
        for k, v in net.items():
            print("接口{}: 接收 {}MB  传输 {}MB".format(k, v.get("Receive"), v.get("Transmit")))

    def disk(self):
        """磁盘空间监控"""
        ssh = self.ssh_command("df -h")
        ssh.expect(pexpect.EOF)
        data = ssh.before.decode("utf-8").strip().split('\n')
        disklists = []
        for disk in data:
            disklists.append(disk.strip().split())
        print("*******************磁盘空间 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        for i in disklists[1:]:
            print("\t文件系统: {}".format(i[0]))
            print("\t容量: {}".format(i[1]))
            print("\t已用: {}".format(i[2]))
            print("\t可用: {}".format(i[3]))
            print("\t已用%挂载点: {}".format(i[4]))

    def com(self):
        """端口监控"""
        ssh = self.ssh_command("netstat -antup | grep '0.0.0.0:'")
        ssh.expect(pexpect.EOF)
        print("*******************端口监控 {}******************".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
        print(ssh.before.decode("utf-8"))


if __name__ == '__main__':
    m = Monitor()
    while True:
        m.memory()
        m.vmstat()
        m.cpu_info()
        m.load()
        m.ionetwork()
        m.disk()
        m.com()
        time.sleep(10)
