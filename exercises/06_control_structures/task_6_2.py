# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip = input('Введите IP-адрес в формате: 10.1.1.0: ')
octets=ip.split('.')
if '255.255.255.255' in ip:
   print('local broadcast')
elif '0.0.0.0' in ip:
   print('unassigned') 
elif int(octets[0]) in range (1,223):
   print('unicast')
elif int(octets[0]) in range (224,239):
   print('multicast')
else:
   print('unused') 
