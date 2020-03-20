# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
ip = input('Введите IP-адрес в формате: 10.1.1.0: ')
octets = ip.split('.')
if len(octets) != 4:
   print('Неправильный IP-адрес, количество октетов не равно 4')
   quit()
elif any(not octet.isdigit() for octet in octets):
   print('Неправильный IP-адрес, один из октетов не является числом')
   quit()
elif any(int(octet) not in range(256) for octet in octets):
   print('Неправильный IP-адрес, один из октетов вне диапазона 0-255')
   quit()
else:
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