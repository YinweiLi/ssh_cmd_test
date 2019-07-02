import paramiko, threading, sys, time, os


class SSHThread(threading.Thread):
    def __init__(self, ip, port, user, pwd, timeout, cmd):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.timeout = timeout
        self.cmd = cmd
        self.LogFile = "/home/linxw/temp/test.log"

    def run(self):
        print("Start try ssh => %s" % self.ip)
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.ip, self.port, username=self.user, password=self.pwd, timeout=self.timeout)
            print("[%s] Login %s => %s " % (self.ip, self.user, self.pwd))
            open(self.LogFile, "a").write("[ %s ] IP => %s, port => %d, %s => %s" % (
            time.asctime(time.localtime(time.time())), self.ip, self.port, self.user, self.pwd))
            print("[%s] exec : %s" % (self.ip, self.cmd))
            open(self.LogFile, "a").write("[%s] exec : %s" % (self.ip, self.cmd))
            stdin, stdout, stderr = ssh.exec_command(self.cmd)
            print("[%s] exec result : %s" % (self.ip, stdout.read()))
            return True
        except:
            print("[%s] Error %s => %s" % (self.ip, self.user, self.pwd))
            open(self.LogFile, "a").write("[%s] Error %s => %s" % (self.ip, self.user, self.pwd))
            return False


def ViolenceSSH(ip, port, user, pwd, timeout, cmd):
    ssh_scan = SSHThread(ip, port, user, pwd, timeout, cmd)
    ssh_scan.start()


if __name__ == '__main__':
    ipList = ['192.168.163.128', '127.0.0.1']
    for ip in ipList:
        threading.Thread(target=ViolenceSSH, args=(ip, 22, 'root', '1234', 3, 'uptime')).start()
