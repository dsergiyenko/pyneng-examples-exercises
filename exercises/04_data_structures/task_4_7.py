# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'
mac_parts=mac.split(':')
binary = bin(int(mac_parts[0], 16)) + bin(int(mac_parts[1], 16)) + bin(int(mac_parts[2], 16)) 
binary = binary.replace('0b', '')
print (binary)