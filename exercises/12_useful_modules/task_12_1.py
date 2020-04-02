# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
addresses = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1']


def ping_ip_addresses(ip_list):
    success_list = []
    fail_list = []
    for address in ip_list:
        code = 1
        code = subprocess.call(["ping", address, "-n", "1"])
        if code == 0:
            success_list.append(address)
        else:
            fail_list.append(address)
    return tuple([success_list, fail_list])

