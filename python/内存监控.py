def memory():
    """内存监控"""
    ssh = ssh_command("192.168.241.101", "root", "123", "cat /proc/meminfo")
    ssh.expect(pexpect.EOF)
    data = re.findall(r"(\d+) kB", ssh.before.decode("utf-8"))  # ssh.before结果为bytes类型，使用utf-8解码为string
    MemTotal = int(data[0]) // 1024  # 除以1024得到MB，整数
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