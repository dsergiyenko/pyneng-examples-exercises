# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

from sys import argv
ip_template = '''{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

ip = argv[1]
net = ip.split('/')[0]
mask = int(ip.split('/')[1])
octet = net.split('.')
bin_mask = '1'*mask+'0'*(32-mask)
#ip address:
na = int(octet[0])
nb = int(octet[1])
nc = int(octet[2])
nd = int(octet[3])
#mask:
ma = int(bin_mask[0:8],2)
mb = int(bin_mask[8:16],2)
mc = int(bin_mask[16:24],2)
md = int(bin_mask[24:32],2)

print('Network:')
print(ip_template.format(na & ma, nb & mb, nc & mc, nd & md))
print('Mask:')
print('/'+str(mask))
print(ip_template.format( ma, mb, mc, md))