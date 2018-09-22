#Or, if you wanted to print from a single host, use this slight edit. That simply removes looking for a list to get the IP address:

from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re
int_down = r"is administratively down"

status = open(r'E:\\Python-Scripts\\python-cisco-status.txt','r+')
old_stdout = sys.stdout
sys.stdout = status
host = '10.0.10.100'
platform = 'cisco_ios'
username = 'javed'
password = 'cisco'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('terminal length 0')
output = device.send_command('enable')
#print('##############################################################\n')
#print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n')
interface_status = device.send_command('show interface Ethernet0/0')
print (interface_status)

interface_result = status.readline()
count = 1
for line in interface_result:
	if int_down in line:
		print ("interface is down")
		break
	else:
		print ("interface is up")
		break
count += 1
status.close()
