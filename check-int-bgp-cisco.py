from __future__ import print_function
from netmiko import ConnectHandler
import pandas as pd

import sys
import time
import select
import paramiko
import re

bgp_result_file = open(r'E:\\Python-Scripts\\bgp-result.txt','r+')
interface_result_file = open(r'E:\\Python-Scripts\\python-cisco-status.txt','r+')
ip_add_file = open(r'E:\\Python-Scripts\\IPAddressList.txt', 'r')
int_down = r"is administratively down"
#data = pd.read_csv('E:\\Python-Scripts\\bgp-status.txt', delim_whitespace=True, header=None)
#with open('E:\\Python-Scripts\\bgp-result.txt') as bgp_result_file:
old_stdout = sys.stdout
sys.stdout = bgp_result_file
sys.stdout = interface_result_file
platform = 'cisco_ios'
username = 'javed'
password = 'cisco'


def check_interface(ip_add_file):
    for host in ip_add_file:
        host = host.rstrip('\n')
        connect = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        output = connect.send_command('terminal length 0')
        output = connect.send_command('enable')
        interface_status = connect.send_command('show interface Ethernet0/0')
        print (interface_status)


def check_bgp(ip_add_file):
    for host in ip_add_file:
        host = host.rstrip('\n')
        connect = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        output = connect.send_command('terminal length 0')
        output = connect.send_command('enable')
        bgp_status = connect.send_command('show ip bgp summary | be N')
        print (bgp_status)
        


def bgp_neighbor_status():
    data = pd.read_csv('E:\\Python-Scripts\\bgp-result.txt', delim_whitespace=True, header=None)
    for index, row in data.iterrows():
        if row[9] == 'Down' or row[9] == 'Idle' or row[9] == 'Active':
            print(f"Neighbor {row[0]} is down")
        else:
            pass
    bgp_result_file.close()



def interface_results(check_interface):
    interface_result = interface_result_file.readline()
    count = 1
    for line in interface_result:
        if int_down in line:
            print ("interface is down")
            break
        else:
            print ("interface is up")
            break
    count += 1
    interface_result_file.close()


check_bgp(ip_add_file)
bgp_neighbor_status()  
interface_results(check_interface)
