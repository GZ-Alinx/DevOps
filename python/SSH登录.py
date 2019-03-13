
def ssh_comand(host, user, password, command):
    """
    SSH登录执行命令
    :param hsot:
    :param user:
    :param password:
    :param command:
    :return:
    """
    ssh = pexpect.spawn('ssh -l {} {} {}'.format(user, host, command))
    i = ssh.expect(['password','continue connecting (yes/no)?'], timeout=8)
    if i == 0:
        ssh.sendline(password)
    if i == 1:
        ssh.sendline('yes')
        ssh.expect('[p,P]assword: ')  # Password/password
        ssh.sendline(password)
    index = ssh.expect(["$", "#", pexpect.EOF, pexpect.TIMEOUT])  # 此处注意，root用户登录符号为#，普通用户为$
    if index != 0:
        print("登录失败！报错内容：{}；{}".format(ssh.before.decode("utf-8"), ssh.after.decode("utf-8")))
        return False
    return ssh