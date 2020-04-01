# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое файла в строку.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

В словаре интерфейсы должны быть записаны без пробела между типом и именем. То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
========================================================
SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R6           Eth 0/5         121           R S I           2811       Eth 0/1
========================================================

'''


def parse_cdp_neighbors(command_output):
    linelist = command_output.split('\n')
    my_host = ''

    list1 = []
    list2 = []
    for line in linelist:
        if '>' in line:
            my_host = line.split('>')[0]
        if 'Eth' in line:
            if (my_host, line.split()[1]+line.split()[2]) in list2:
                continue
            else:
                list1.append((my_host, line.split()[1]+line.split()[2]))
                list2.append((line.split()[0], line.split()[-2]+line.split()[-1]))
    return dict(zip(list1, list2))

if __name__ == '__main__':
    lines = ''
    with open('sh_cdp_n_r3.txt', 'r') as f:
        lines = f.read()

    parse_cdp_neighbors(lines)
