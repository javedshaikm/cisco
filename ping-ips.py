import subprocess

ip_list = list(set(open("D:\\python\\sdc-ip.txt").read().splitlines()))
reach = []
not_reach = []
for i, ip_address in enumerate(ip_list):
    response = subprocess.call(['ping', '-n', '2', ip_address])
    if response == 0:
        reach.append(f"{i + 1}. {ip_address} is reachable\n")
    else:
        not_reach.append(f"{i + 1}. {ip_address} is not reachable\n")

with open('D:\\python\\ping_reachable.txt', 'a') as f_reach, open('D:\\python\\ping_unreachable.txt', 'a') as f_not_reach:
    f_reach.write(''.join(reach))
    f_not_reach.write(''.join(not_reach))
