# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
ip_is_correct = False
while not ip_is_correct:
    ip = input('Введите IP-адрес в формате: 10.1.1.0: ')
    octets = ip.split('.')
    if len(octets) != 4:
       print('Неправильный IP-адрес, количество октетов не равно 4')
       continue
    elif any(not octet.isdigit() for octet in octets):
       print('Неправильный IP-адрес, один из октетов не является числом')
       continue
    elif any(int(octet) not in range(256) for octet in octets):
       print('Неправильный IP-адрес, один из октетов вне диапазона 0-255')
       continue
    else:
       ip_is_correct = True
       if '255.255.255.255' in ip:
          print('local broadcast')
       elif '0.0.0.0' in ip:
          print('unassigned')
       elif int(octets[0]) in range(1, 224):
          print('unicast')
       elif int(octets[0]) in range(224, 240):
          print('multicast')
       else:
          print('unused')