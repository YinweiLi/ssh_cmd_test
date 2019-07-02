import paramiko
import time


def ssh(ip,port,user,passwd,cmd):

    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        sshclient.connect(ip,port,user,passwd,timeout=5)
        print(time.time())
        print('****************%s is connected******************** \n' %(ip))

        ssh_shell = sshclient.invoke_shell()
        i = 0

        while True:
            i += 1
            print(i)
            line = ssh_shell.recv(1024)
            print('standard out----->', i, line)
            # end = ['#','#']
            l = str(line)
            if line and l.endswith("#'"):
                print('break')
                break
        lines = []
        for c in cmd:
            print('执行此命令：')
            print(c)
            time.sleep(0.1)
            if c.startswith('write'):
                ssh_shell.send(c)
                time.sleep(0.5)
                ssh_shell.send('y\n')
                print("send yes!!!!!")
            else:
                ssh_shell.sendall(c)

            while True:
                i = i + 1
                print(i)
                line = ssh_shell.recv(1024)
                # end = ['#','#']
                l = str(line)
                lines.append(line)
                print(l)
                if line and l.endswith("#'"):
                    break
            result = ''
            result = result + str(lines)
            print('result----->', result)
        for ll in lines:
            print(ll)

        sshclient.close()
        print('***************ssh:',ip,' is closed***************')
    except Exception as e:
        print(e+'Error!!!!!!!')

if __name__ == '__main__':

    print('*********************start**********************')
    #ipAddr = ['192.168.253.1', '192.168.253.2', '192.168.253.3']
    #ipAddr = '192.168.253.2'
    #需要配置的sshIP
    ipAddr = [
        # '192.168.253.1',
        # '192.168.253.2',
        # '192.168.253.3',
        '192.168.253.4',
        '192.168.253.5',
        '192.168.253.6',
        '192.168.253.65',
        '192.168.253.66',
        '192.168.253.67'
    ]
    username = "***"  # 用户名

    passwd = "******"  # 密码

    # cmd = ['echo i am your a girl5>> /home/test.txt','cat /home/test.txt']

    #cmd = 'ping 192.168.70.245'+'\n'
    cmd1 = 'configure'+'\n'
    cmd2 = 'snmp trap-server 192.168.159.78 162 ZWzabbix123 v2'+'\n'
    cmd3 = 'exit'+'\n'
    cmd4 = 'write file'+'\n'
    #cmd5 = 'y'+'\n'#endwith   [y]
    cmd5 = 'no filter-list global in 2002'+'\n'
    cmd6 = 'filter-list 2002'+'\n'
    cmd7 = 'filter 4 tcp 192.168.159.0/24 any 192.168.253.0/24 161'+'\n'
    cmd8 = 'filter 4 action permit'+'\n'
    cmd9 = 'filter 8 udp 192.168.159.0/24 any 192.168.253.0/24 161'+'\n'
    cmd10 = 'filter 8 action permit'+'\n'
    cmd11 = 'exit'+'\n'
    cmd12 = 'filter-list global in 2002'+'\n'
    cmd13 = 'exit'+'\n'
    cmd14 = 'write file'+'\n'

    #cmd = [cmd1,cmd2,cmd3,cmd4]
    #cmd = [cmd1,cmd3,cmd4]
    #命令依次添加到列表中
    cmd = [cmd1,cmd2,cmd5,cmd6,cmd7,cmd8,cmd9,cmd10,cmd11,cmd12,cmd13,cmd14]
	#单线程执行循环配置
    for ip in ipAddr:
        ssh(ip, 22, username, passwd, cmd)


    print('*******************the end ****************')



