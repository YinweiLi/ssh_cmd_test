# coding=utf-8
import sys
import os

ipAddr = [
        '192.168.146.2',
        '192.168.51.32'
    ]
list1 = []
listOK = []
listERROR = []
for ip in ipAddr:
    retu = os.system('ping -n 1 -w 1 %s'%ip)
    if retu:
        #print(ip,'ERROR')
        l = str(ip)+'---ERROR'
        list1.append(l)
        listERROR.append(l)
    else:
        #print(ip,'OK')
        l = str(ip) + '---OK'
        list1.append(l)
        listOK.append(l)
i = 0
for ll in list1:
    print(ll)
    i = i + 1
print('total:',i,'  OK:',listOK.__len__(),'   ERROR',listERROR.__len__())

