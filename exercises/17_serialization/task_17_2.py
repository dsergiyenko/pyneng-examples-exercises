# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''


import re
from pprint import pprint


def parse_sh_cdp_neighbors(filename):
    with open(filename) as f:
        command_output = f.read()
    hostname = re.findall(r'(\S+)>', command_output)
    result = re.findall(r'(\S+) +(\S+ \d+/\d+).+ (\S+ \d+/\d+)\n', command_output)
    result_dict = {}
    result_dict.update({ hostname[0] : {} })
    for link in result:
         result_dict[hostname[0]].update({link[1]: {link[0]: link[2]}})
    return result_dict


if __name__ == '__main__':
    parse_sh_cdp_neighbors('sh_cdp_n_sw1.txt')