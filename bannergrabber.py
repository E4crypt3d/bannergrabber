#!/usr/bin/python3
import socket
import sys
soc = socket.socket()
print('''               LITTLE BANNER GRABBER
                        LG҉B҉
                Created by @E4crypt3d''')
ip = input("Enter the IP: ")
port = str(input('Port No: '))
try:
    soc.connect((ip,int(port)))
except socket.error as e:
    print("Port Closed or Firewall is Blocking Us")
    sys.exit(1)
ban = soc.recv(2048)
bann = str(ban)
banne = bann.replace('\\n','')
banner = banne.replace('\\r','')
print(banner.strip('b'))