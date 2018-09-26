import paramiko
import socket
dssh = paramiko.SSHClient()
dssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ips = [i.strip() for i in open("C:\Python27\Testing\Fetch.txt")] # creates a list from input file

for ip in ips:
    try:
        dssh.connect(ip, username='cisco', password='cisco', timeout=4)
        stdin, stdout, stderr = ssh.exec_command('sh ip ssh')
        print ip + '===' + stdout.read()
        ssh.close()
    except paramiko.AuthenticationException:
        print ip + '=== Bad credentials'
    except paramiko.SSHException:
        print ip + '=== Issues with ssh service'
    except socket.error:
        print ip + '=== Device unreachable' 
