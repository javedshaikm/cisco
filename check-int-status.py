from __future__ import print_function
from netmiko import ConnectHandler
import pandas as pd
import smtplib
import sys
import time
import select
import paramiko
import re

username = 'cisco'
password = 'cisco_1234!'
int_down = r"is administratively down"
hosts = ['10.10.20.48']
interfaces_1 = ['GigabitEthernet1','GigabitEthernet2','GigabitEthernet3']
platform = 'cisco_xe'

for host in hosts:
	connect = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
	output = connect.send_command('terminal length 0',expect_string='csr1000v')
	#output = connect.send_command('enable')
	if host == '10.10.20.48':
		for interfaces in interfaces_1:
			interface_status = connect.send_command(f'show interface {interfaces}',expect_string='csr1000v')
			#print(host)
			#print(interfaces)
			
			#print (interface_status)
			for line in interface_status.split('\n'):
				#print (line)
				#if 'Description' in line:
				#	pass
				if int_down in line:
					print(f"{interfaces} is down in {host}")

				else:
					pass
					#print('All interfaces are up')
					#break

                	
