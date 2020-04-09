# -*- coding: utf-8 -*-
'''
Задание 17.2a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

'''
import glob
import re
import csv
from pprint import pprint
import yaml


sh_version_files = glob.glob('sh_cdp_n*')
print(sh_version_files)

import re
from pprint import pprint


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    result_dict = {}
    for my_file in list_of_files:
        with open(my_file) as f:
            command_output = f.read()
        hostname = re.findall(r'(\S+)>', command_output)
        result = re.findall(r'(\S+) +(\S+ \d+/\d+).+ (\S+ \d+/\d+)\n', command_output)
        result_dict.update({ hostname[0] : {} })
        for link in result:
             result_dict[hostname[0]].update({link[1]: {link[0]: link[2]}})
    pprint( result_dict )
    if save_to_filename:
        with open(save_to_filename, 'w') as f_out:
            yaml.dump(result_dict, f_out)
    return result_dict


if __name__ == '__main__':
    generate_topology_from_cdp(sh_version_files)