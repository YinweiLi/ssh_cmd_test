
  import sys
  import telnetlib
  import time
  
  HOST ="192.168.1.103"
  USER = b"administrator"
  PASS = b"1"
  cmd=b" dir rn" #此处也可以为ipconfig
  tn = telnetlib.Telnet(HOST)
  tn.set_debuglevel(0)
  print("正在加载文件，请稍等……")
  #休眠5秒，不然第二次读取也可能读不出来
  time.sleep(5)
  #当匹配到login时代表已成功连接到HOST主机，这儿为输入帐号提示
  tn.read_until(b"login:")
  #向主机发送登陆帐号，模拟键盘输入 
  tn.write(USER+b"rn")
  #print("login success");
  #向主机发送登陆密码，模拟键盘输入 
  tn.read_until(b"password:")
  tn.write(PASS+b"rn")
  #print("password success");
  #判断是否成功登陆主机
  tn.read_until(b"Microsoft Telnet Server")
  #向主机发送相应的DOS命令行
  tn.write(cmd+b"rn")
  #print("cmd success");
  tn.write(b"exitrn")
  #读取所匹配到的数据
  ra=tn.read_all()
  #print(type(ra));
  print(ra.decode('gbk'))
  tn.close()
  print("获取结束……")
  