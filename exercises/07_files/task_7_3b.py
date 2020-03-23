# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
vlan = input('Введите номер vlan: ')
mac_list = []
with open('CAM_table.txt', 'r') as f:
    for line in f:
        line_list = line.split('   ')
        if line_list[0][1:].isdigit():
            mac_list.append([line_list[0][1:] , line_list[1], line_list[3].rstrip()] )
for list in mac_list:
    if list[0] == vlan:
        print ('    '.join( list ))