# -*- coding: utf-8 -*-
'''
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re
from pprint import pprint

#checked in windows
def get_ip_from_cfg(filename):
    result_dict={}
    config = open('config_r2.txt').read()
    result = re.findall(r'interface (.+)(.*\n){0,3} ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)', config)
    result2 = re.findall(r'interface (.+)(.*\n){0,3} ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+).*\n ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+) secondary', config)
    if result:
        for interface, trash, ip, mask in result:
            result_dict.update({interface:[(ip,mask)]})
    if result2:
        for interface, trash, ip, mask, ip_second, mask_second in result2:
            result_dict.update({interface:[(ip,mask),(ip_second,mask_second)]})

    return result_dict


if __name__ == '__main__':
    pprint( get_ip_from_cfg('config_r2.txt') )