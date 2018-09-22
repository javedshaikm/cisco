from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re
fd = open(r'C:\Users\NewdayTest.txt','w') 
old_stdout = sys.stdout   
sys.stdout = fd 
platform = 'cisco_ios'
username = 'Username'
password = 'Password'

ip_add_file = open(r'C:\\Users\\IPAddressList.txt','r') 

for host in ip_add_file:
    device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
    output = device.send_command('terminal length 0')
    output = device.send_command('enable')
    print('##############################################################\n')
    print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n')
    output = device.send_command('sh run')
    print(output)
    print('##############################################################\n')
    print('...................CISCO COMMAND SHOW IP INT BR OUTPUT......................\n')
    output = device.send_command('sh ip int br')
    print(output) 
    print('##############################################################\n')

fd.close()

