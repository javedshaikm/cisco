ip_list = open("D:\\python\\sdc-ip.txt").read().splitlines()

ip_list = list(set(ip_list))
import os
i=1
j=1
reach=[]
not_reach=[]
#for n, ip_address in enumerate(ip_list):
for ip_address in ip_list:
    response = os.system("ping -n 2 " + ip_address)
    if response == 0:
        reach.append('{}. {} is reachable\n'.format(i,ip_address))
        i+=1
    else:
        not_reach.append('{}. {} is not reachable\n'.format(j,ip_address))
        j+=1

with open('D:\\python\\ping_reachable.txt', 'a') as f:
    for i in reach:
        f.write(i)

with open('D:\\python\\ping_unreachable.txt', 'a') as  f:
    for i in not_reach:
        f.write(i)
