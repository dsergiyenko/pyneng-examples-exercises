# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-сеть в формате: 10.1.1.0/24: ')
net = ip.split('/')[0]
mask = int(ip.split('/')[1])
octet = net.split('.')

print('Network:')
print("{:10} {:10} {:10} {:10}".format(octet[0], octet[1], octet[2], octet[3]))
print("{:10} {:10} {:10} {:10}".format(  format(int(octet[0]), '08b') , format(int(octet[1]), '08b')  , format(int(octet[2]), '08b') , format(int(octet[3]), '08b') ))
print('\n')
print('Mask:')
print('/'+str(mask))
bin_mask = '1'*mask+'0'*(32-mask)
print("{:10} {:10} {:10} {:10}".format(str(int(bin_mask[0:8],2)), str(int(bin_mask[8:16],2)), str(int(bin_mask[16:24],2)), str(int(bin_mask[24:32],2))))
print("{:10} {:10} {:10} {:10}".format(bin_mask[0:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:32]))