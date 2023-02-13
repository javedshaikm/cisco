from netmiko import ConnectHandler

platform = 'cisco_ios'
username = 'Username'
password = 'Password'
commands = ['terminal length 0', 'enable', 'show run', 'show ip int br']

with open('C:\\Users\\NewdayTest.txt', 'w') as fd:
    for host in open('C:\\Users\\IPAddressList.txt', 'r'):
        with ConnectHandler(device_type=platform, ip=host.strip(), username=username, password=password) as device:
            print('##############################################################\n', file=fd)
            print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n', file=fd)
            output = device.send_command(commands[2])
            print(output, file=fd)
            print('##############################################################\n', file=fd)
            print('...................CISCO COMMAND SHOW IP INT BR OUTPUT......................\n', file=fd)
            output = device.send_command(commands[3])
            print(output, file=fd) 
            print('##############################################################\n', file=fd)
