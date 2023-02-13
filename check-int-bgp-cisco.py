from __future__ import print_function
from netmiko import ConnectHandler
import pandas as pd

import sys
import time
import select
import paramiko
import re

bgp_result_path = r'E:\\Python-Scripts\\bgp-result.txt'
interface_result_path = r'E:\\Python-Scripts\\python-cisco-status.txt'
ip_add_file_path = r'E:\\Python-Scripts\\IPAddressList.txt'

platform = 'cisco_ios'
username = 'javed'
password = 'cisco'

def check_interface(ip_add_file):
    for host in ip_add_file:
        host = host.rstrip('\n')
        with ConnectHandler(device_type=platform, ip=host, username=username, password=password) as connect:
            output = connect.send_command('terminal length 0')
            output = connect.send_command('enable')
            interface_status = connect.send_command('show interface Ethernet0/0')
            print(interface_status)

def check_bgp(ip_add_file):
    for host in ip_add_file:
        host = host.rstrip('\n')
        with ConnectHandler(device_type=platform, ip=host, username=username, password=password) as connect:
            output = connect.send_command('terminal length 0')
            output = connect.send_command('enable')
            bgp_status = connect.send_command('show ip bgp summary | be N')
            print(bgp_status)

def bgp_neighbor_status():
    with open(bgp_result_path) as bgp_result_file:
        data = pd.read_csv(bgp_result_file, delim_whitespace=True, header=None)
        for index, row in data.iterrows():
            if row[9] == 'Down' or row[9] == 'Idle' or row[9] == 'Active':
                print(f"Neighbor {row[0]} is down")
        bgp_result_file.close()

def interface_results():
    with open(interface_result_path) as interface_result_file:
        for count, line in enumerate(interface_result_file):
            if int_down in line:
                print("interface is down")
                break
        else:
            print("interface is up")
        interface_result_file.close()

with open(ip_add_file_path) as ip_add_file:
    check_bgp(ip_add_file)
    bgp_neighbor_status()
    check_interface(ip_add_file)

interface_results()

