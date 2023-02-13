from netmiko import ConnectHandler
import logging

# Set up logging
logging.basicConfig(filename='interface_status.log', level=logging.INFO)

username = 'cisco'
password = 'cisco_1234!'
int_down = r"is administratively down"

# Read hosts and interfaces from a file or database
hosts = ['10.10.20.48']
interfaces = ['GigabitEthernet1', 'GigabitEthernet2', 'GigabitEthernet3']

platform = 'cisco_xe'

for host in hosts:
    try:
        connect = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
        output = connect.send_command('terminal length 0', expect_string='csr1000v')

        for interface in interfaces:
            interface_status = connect.send_command(f'show interface {interface}', expect_string='csr1000v')

            for line in interface_status.split('\n'):
                if int_down in line:
                    logging.info(f"{interface} is down in {host}")
                else:
                    pass
        connect.disconnect()

    except Exception as e:
        logging.error(f"Error occurred while checking interfaces on {host}: {e}")

                	
