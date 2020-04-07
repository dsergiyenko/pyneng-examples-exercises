# -*- coding: utf-8 -*-
'''
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'

SW1>show cdp neighbors

Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater, P - Phone

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R1           Eth 0/1         122           R S I           2811       Eth 0/0
R2           Eth 0/2         143           R S I           2811       Eth 0/0
R3           Eth 0/3         151           R S I           2811       Eth 0/0
R6           Eth 0/5         121           R S I           2811       Eth 0/1
Проверить работу функции на файле sh_cdp_n_sw1.txt.
'''

import re
from pprint import pprint


def generate_description_from_cdp(filename):
    with open('sh_cdp_n_sw1.txt') as f:
        command_output = f.read()

    result = re.findall(r'(\S+) +(\S+ \d+/\d+).+ (\S+ \d+/\d+)\n', command_output)
    result_dict = {}
    for link in result:
        result_dict.update({link[1]: 'description Connected to '+link[0]+' port '+link[2]})

    return result_dict


if __name__ == '__main__':
    generate_description_from_cdp('sh_cdp_n_sw1.txt')