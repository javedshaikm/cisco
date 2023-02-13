import paramiko
import socket

ips = [i.strip() for i in open("C:\Python27\Testing\Fetch.txt")]

for ip in ips:
    with paramiko.SSHClient() as ssh:
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(ip, username='cisco', password='cisco', timeout=4)
            stdin, stdout, stderr = ssh.exec_command('sh ip ssh')
            print ip + '===' + stdout.read()
        except paramiko.AuthenticationException:
            print ip + '=== Bad credentials'
        except paramiko.SSHException:
            print ip + '=== Issues with ssh service'
        except socket.error:
            print ip + '=== Device unreachable'
