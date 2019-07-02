import paramiko
import time


def ssh(ip,port,user,passwd,cmd):

    try:
        #paramiko连接ssh主机
        sshclient = paramiko.SSHClient()
        sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        sshclient.connect(ip,port,user,passwd,timeout=12)
        print(time.time())
        print('****************%s is connected******************** \n' %(ip))
        #获取ssh控制台
        ssh_shell = sshclient.invoke_shell()
        i = 0

        #获取控制台输出字符串，循环判断是否为结束符'#'
        #如果是，跳出循环，进行下面操作
        while True:
            i += 1
            print(i)
            line = ssh_shell.recv(1024)
            print('standard out----->', i, line)
            # end = ['#','#']
            l = str(line)
            if line and l.endswith(">'"):
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
                if line and l.endswith(">'"):
                    break
            #result = ''
            #result = result + str(lines)
            #print('result----->', result)
        for ll in lines:
            print(ll)

        sshclient.close()
        print('***************ssh:',ip,' is closed***************')
    except Exception as e:
        print('********'+'Error!!!!!!!'+ip+'!!!!!!!!!!!!!!*******')
        print(e)
        return False
    else:
        print('******************** '+ip+'--OK ************************')

    finally:
        print('******************NEXT**********************')
        return True

if __name__ == '__main__':

    print('*********************start**********************')
    #ipAddr = ['192.168.253.1', '192.168.253.2', '192.168.253.3']
    #ipAddr = '192.168.48.203'
    #需要配置的sshIP
    ipAddr = [
        '192.168.48.201',
        '192.168.48.202',
        '192.168.48.203',
        '192.168.48.204',
        '192.168.48.205',
        '192.168.48.206',
        '192.168.48.207',
        '192.168.48.208',
        '192.168.48.209',
        '192.168.48.210',
        '192.168.48.211',
        '192.168.48.212',
        '192.168.48.213',
        '192.168.48.214',
        '192.168.48.215',
        '192.168.48.216',
        '192.168.48.217',
        '192.168.48.218',
        '192.168.48.219',
        '192.168.48.220',
        '192.168.48.221',
        '192.168.48.222',
        '192.168.48.223',
        '192.168.48.224',
        '192.168.48.225',
        '192.168.48.226',
        '192.168.48.227',
        '192.168.48.228',
        '192.168.48.229',
        '192.168.48.230',
        '192.168.48.231',
        '192.168.48.232',
        '192.168.48.233',
        '192.168.48.234',
        '192.168.48.235',
        '192.168.48.236',
        '192.168.48.237',
        '192.168.48.238',
        '192.168.48.239',
        '192.168.48.240',
        '192.168.48.241',
        '192.168.48.242',
        '192.168.48.243',
        '192.168.48.244',
        '192.168.48.245',
        '192.168.48.246',
        '192.168.48.247',
        '192.168.48.248',
        '192.168.48.249',
        '192.168.48.250',
        '192.168.49.1',
        '192.168.49.2',
        '192.168.49.3',
        '192.168.49.4',
        '192.168.49.5',
        '192.168.49.6',
        '192.168.49.7',
        '192.168.49.8',
        '192.168.49.9',
        '192.168.49.10',
        '192.168.49.11',
        '192.168.49.12',
        '192.168.49.13',
        '192.168.49.14',
        '192.168.49.15',
        '192.168.49.16',
        '192.168.49.17',
        '192.168.49.18',
        '192.168.49.19',
        '192.168.49.20',
        '192.168.49.21',
        '192.168.49.22',
        '192.168.49.23',
        '192.168.49.24',
        '192.168.49.25',
        '192.168.49.26',
        '192.168.49.27',
        '192.168.49.28',
        '192.168.49.29',
        '192.168.49.30',
        '192.168.49.31',
        '192.168.49.32',
        '192.168.49.33',
        '192.168.49.34',
        '192.168.49.35',
        '192.168.49.36',
        '192.168.49.37',
        '192.168.49.38',
        '192.168.49.39',
        '192.168.49.40',
        '192.168.49.41',
        '192.168.49.42',
        '192.168.49.43',
        '192.168.49.44',
        '192.168.49.45',
        '192.168.49.46',
        '192.168.49.47',
        '192.168.49.48',
        '192.168.49.49',
        '192.168.49.50',
        '192.168.49.113',
        '192.168.49.114',
        '192.168.49.115',
        '192.168.49.116',
        '192.168.49.117',
        '192.168.49.118',
        '192.168.49.119',
        '192.168.49.120',
        '192.168.49.121',
        '192.168.49.122',
        '192.168.49.123',
        '192.168.49.124',
        '192.168.49.125',
        '192.168.49.126',
        '192.168.49.127',
        '192.168.49.128',
        '192.168.49.129',
        '192.168.49.130',
        '192.168.49.131',
        '192.168.49.132',
        '192.168.49.133',
        '192.168.49.134',
        '192.168.49.135',
        '192.168.49.136',
        '192.168.49.137',
        '192.168.49.138',
        '192.168.49.139',
        '192.168.49.140',
        '192.168.49.141',
        '192.168.49.142',
        '192.168.49.143',
        '192.168.49.144',
        '192.168.49.145',
        '192.168.49.146',
        '192.168.49.147',
        '192.168.49.148',
        '192.168.49.149',
        '192.168.49.150',
        '192.168.49.151',
        '192.168.49.152',
        '192.168.49.153',
        '192.168.49.154',
        '192.168.49.155',
        '192.168.49.156',
        '192.168.49.157',
        '192.168.49.158',
        '192.168.49.159',
        '192.168.49.160',
        '192.168.49.161',
        '192.168.49.162',
        '192.168.49.163',
        '192.168.49.164',
        '192.168.49.165',
        '192.168.49.166',
        '192.168.49.167',
        '192.168.49.168',
        '192.168.49.169',
        '192.168.49.170',
        '192.168.49.171',
        '192.168.49.172',
        '192.168.49.173',
        '192.168.49.174',
        '192.168.49.175',
        '192.168.49.176',
        '192.168.49.177',
        '192.168.49.178',
        '192.168.49.179',
        '192.168.49.180',
        '192.168.49.181',
        '192.168.49.182',
        '192.168.49.183',
        '192.168.49.184',
        '192.168.49.185',
        '192.168.49.186',
        '192.168.49.187',
        '192.168.49.188',
        '192.168.49.189',
        '192.168.49.190',
        '192.168.49.191',
        '192.168.49.192',
        '192.168.49.193',
        '192.168.49.194',
        '192.168.49.195',
        '192.168.49.196',
        '192.168.49.197',
        '192.168.49.198',
        '192.168.49.199',
        '192.168.49.200',
        '192.168.49.201',
        '192.168.49.202',
        '192.168.49.203',
        '192.168.49.204',
        '192.168.49.205',
        '192.168.49.206',
        '192.168.49.207',
        '192.168.49.208',
        '192.168.49.209',
        '192.168.49.210',
        '192.168.49.211',
        '192.168.49.212',
        '192.168.49.213',
        '192.168.49.214',
        '192.168.49.215',
        '192.168.49.216',
        '192.168.49.217',
        '192.168.49.218',
        '192.168.49.219',
        '192.168.49.220',
        '192.168.49.221',
        '192.168.49.222',
        '192.168.49.223',
        '192.168.49.224',
        '192.168.49.225',
        '192.168.49.226',
        '192.168.49.227',
        '192.168.49.228',
        '192.168.49.229',
        '192.168.49.230',
        '192.168.49.231',
        '192.168.49.232',
        '192.168.49.233',
        '192.168.49.234',
        '192.168.49.235',
        '192.168.49.236',
        '192.168.49.237',
        '192.168.49.238',
        '192.168.49.239',
        '192.168.49.240',
        '192.168.49.241',
        '192.168.49.242',
        '192.168.49.243',
        '192.168.49.244',
        '192.168.49.245',
        '192.168.49.246',
        '192.168.49.247',
        '192.168.49.248',
        '192.168.49.249',
        '192.168.49.250',
        '192.168.50.1',
        '192.168.50.2',
        '192.168.50.3',
        '192.168.50.4',
        '192.168.50.5',
        '192.168.50.6',
        '192.168.50.7',
        '192.168.50.8',
        '192.168.50.9',
        '192.168.50.10',
        '192.168.50.11',
        '192.168.50.12',
        '192.168.50.13',
        '192.168.50.14',
        '192.168.50.15',
        '192.168.50.16',
        '192.168.50.17',
        '192.168.50.18',
        '192.168.50.19',
        '192.168.50.20',
        '192.168.50.21',
        '192.168.50.22',
        '192.168.50.23',
        '192.168.50.24',
        '192.168.50.25',
        '192.168.50.26',
        '192.168.50.27',
        '192.168.50.28',
        '192.168.50.29',
        '192.168.50.30',
        '192.168.50.31',
        '192.168.50.32',
        '192.168.50.33',
        '192.168.50.34',
        '192.168.50.35',
        '192.168.50.36',
        '192.168.50.37',
        '192.168.50.38',
        '192.168.50.39',
        '192.168.50.40',
        '192.168.50.41',
        '192.168.50.42',
        '192.168.50.43',
        '192.168.50.44',
        '192.168.50.45',
        '192.168.50.46',
        '192.168.50.47',
        '192.168.50.48',
        '192.168.50.49',
        '192.168.50.50',
        '192.168.50.51',
        '192.168.50.52',
        '192.168.50.53',
        '192.168.50.54',
        '192.168.50.55',
        '192.168.50.56',
        '192.168.50.57',
        '192.168.50.58',
        '192.168.50.59',
        '192.168.50.60',
        '192.168.50.61',
        '192.168.50.62',
        '192.168.50.63',
        '192.168.50.64',
        '192.168.50.65',
        '192.168.50.66',
        '192.168.50.67',
        '192.168.50.68',
        '192.168.50.69',
        '192.168.50.70',
        '192.168.50.71',
        '192.168.50.72',
        '192.168.50.73',
        '192.168.50.74',
        '192.168.50.75',
        '192.168.50.76',
        '192.168.50.77',
        '192.168.50.78',
        '192.168.50.79',
        '192.168.50.80',
        '192.168.50.81',
        '192.168.50.82',
        '192.168.50.83',
        '192.168.50.84',
        '192.168.50.85',
        '192.168.50.86',
        '192.168.50.87',
        '192.168.50.88',
        '192.168.50.89',
        '192.168.50.90',
        '192.168.50.91',
        '192.168.50.92',
        '192.168.50.93',
        '192.168.50.94',
        '192.168.50.95',
        '192.168.50.96',
        '192.168.50.97',
        '192.168.50.98',
        '192.168.50.99',
        '192.168.50.100',
        '192.168.50.101',
        '192.168.50.102',
        '192.168.50.103',
        '192.168.50.104',
        '192.168.50.105',
        '192.168.50.106',
        '192.168.50.107',
        '192.168.50.108',
        '192.168.50.109',
        '192.168.50.110',
        '192.168.50.111',
        '192.168.50.112',
        '192.168.50.113',
        '192.168.50.114',
        '192.168.50.115',
        '192.168.50.116',
        '192.168.50.117',
        '192.168.50.118',
        '192.168.50.119',
        '192.168.50.120',
        '192.168.50.121',
        '192.168.50.122',
        '192.168.50.123',
        '192.168.50.124',
        '192.168.50.125',
        '192.168.50.126',
        '192.168.50.127',
        '192.168.50.128',
        '192.168.50.129',
        '192.168.50.130',
        '192.168.50.131',
        '192.168.50.132',
        '192.168.50.133',
        '192.168.50.134',
        '192.168.50.135',
        '192.168.50.136',
        '192.168.50.137',
        '192.168.50.138',
        '192.168.50.139',
        '192.168.50.140',
        '192.168.50.141',
        '192.168.50.142',
        '192.168.50.143',
        '192.168.50.144',
        '192.168.50.145',
        '192.168.50.146',
        '192.168.50.147',
        '192.168.50.148',
        '192.168.50.149',
        '192.168.50.150',
        '192.168.50.151',
        '192.168.50.152',
        '192.168.50.153',
        '192.168.50.154',
        '192.168.50.155',
        '192.168.50.156',
        '192.168.50.157',
        '192.168.50.158',
        '192.168.50.159',
        '192.168.50.160',
        '192.168.50.161',
        '192.168.50.162',
     ]
    #ipAddr = ['192.168.48.201','192.168.48.202']
    username = "********"  # 用户名

    passwd = "********"  # 密码



    cmd1 = 'ipmcset -t service -d state -v SSH disabled' + '\n'
    cmd2 = 'route'+'\n'
    #cmd = [cmd1,cmd2,cmd3,cmd4]
    cmd = [cmd1]
    #命令依次添加到列表中
    #cmd = [cmd1,cmd2,cmd5,cmd6,cmd7,cmd8,cmd9,cmd10,cmd11,cmd12,cmd13,cmd14]
	#单线程执行循环配置
    for ip in ipAddr:
        ssh(ip, 22, username, passwd, cmd)


    print('*******************the end ****************')


