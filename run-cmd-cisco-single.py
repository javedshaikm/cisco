from netmiko import ConnectHandler

platform = 'cisco_ios'
username = 'cisco'
password = 'cisco'
host = '10.0.10.100'
interface = 'Ethernet0/0'
int_down = 'is administratively down'

with ConnectHandler(device_type=platform, ip=host, username=username, password=password) as device:
    device.send_command('terminal length 0')
    device.send_command('enable')
    interface_status = device.send_command(f'show interface {interface}')
    print(interface_status)
    if int_down in interface_status:
        print(f"{interface} is down")
    else:
        print(f"{interface} is up")
