import paramiko
import time


def ssh(ip,port,user,passwd,cmd):

    try:
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        sshclient.connect(ip,port,user,passwd,timeout=5)
        print(time.time())
        print('%s is connected \n' %(ip))

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

        for c in cmd:
            print('执行此命令：')
            print(c)

            ssh_shell.sendall(c)
            lines = []
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
            #print('result----->', result)
            for ll in lines:
                print(ll)

        sshclient.close()
    except Exception as e:
        print(e+'Error!!!!!!!')

if __name__ == '__main__':

    #ipAddr = ['192.168.253.1', '192.168.253.2', '192.168.253.3']
    ipAddr = '192.168.253.1'

    username = "***"  # 用户名

    passwd = "*******"  # 密码

    # cmd = ['echo i am your a girl5>> /home/test.txt','cat /home/test.txt']

    #cmd = 'ping 192.168.70.245'+'\n'
    cmd1 = 'configure'+'\n'
    cmd2 = 'snmp trap-server 192.168.159.78 162 ZWzabbix123 v2'+'\n'
    cmd3 = 'exit'+'\n'
    cmd4 = 'write file'+ '\n' + 'y'+'\n'
    #cmd5 = 'y'+'\n'#endwith   [y]
    #cmd = [cmd1,cmd2,cmd3,cmd4]
    cmd = [cmd1,cmd3]

    ssh(ipAddr,22,username,passwd,cmd)


#client = paramiko.SSHClient()
#client.load_system_host_keys()

# connect to client
#client.connect('192.168.253.1', 22, 'admin', 'Flzx3qc!Ysyhl9t!', allow_agent=False, look_for_keys=False)

# get shell
#ssh_shell = client.invoke_shell()
# ready when line endswith '>' or other character
#while True:
 #   line = ssh_shell.recv(1024)
    # print line
 #   if line and line.endswith('#'):
  #      break;

# send command
#ssh_shell.sendall('ping 192.168.70.245' + '\n')

# get result lines
#lines = []
#while True:
 #   line = ssh_shell.recv(1024)
  #  if line and line.endswith('>'):
   #     break;
    #lines.append(line)
#result = ''.join(lines)

# print result
#print(result)

#ssh_shell.close()

