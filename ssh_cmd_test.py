
import paramiko

import threading

def ssh2(ip,username,passwd,cmd):

    try:
        file = open('sshcmdtest_log.txt','a')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        print('%s ssh is connected\n'%(ip))
        for m in cmd:
            print(m)
            stdin, stdout, stderr = ssh.exec_command(m)
            stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            print(out)
            for o in out:
                print(o)
            print('%s    OK\n' % (m))
        print('%s exceted cmd OK'%(ip))
        ssh.close()
        print(ip, 'ssh is closed')
        logMeg = str(ip) + ' exceted cmd OK\n' + str(ip) + ' ssh is closed\n'
        file.write(logMeg)
        file.close()


    except Exception as e:
        print('%s\tError\n' % (ip),e)
        file = open('sshcmdtest_log.txt', 'a')
        logMeg = str(ip) + ' have some Exception when cinnected\n'
        file.write(logMeg)
        file.close()




if __name__=='__main__':

    ipAddr = ['10.200.1.241','10.200.1.242','10.200.1.243']

    username = "root"  #用户名

    passwd = "******"    #密码

    cmd = ['echo i am your a girl5>> /home/test.txt','cat /home/test.txt']

    #cmd = ['cd /\r','cd home\r','echo no you a girl2>> test.txt']#你要执行的命令列表

    threads = []   #多线程

    print("Begin......")

    for ip in ipAddr:
        print(ip)
        t = threading.Thread(target=ssh2,args=(ip,username,passwd,cmd))
        threads.append(t)


    for t in threads:
        print(t)
        t.setDaemon(True)
        #将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
        t.start()

    waitTime = input()
    print(waitTime)

    #ssh2(ip,username,passwd,cmd)

    print('end!!!!!!!')



