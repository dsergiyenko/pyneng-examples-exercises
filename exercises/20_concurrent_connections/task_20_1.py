# -*- coding: utf-8 -*-
'''
Задание 20.1

Создать функцию ping_ip_addresses, которая проверяет доступность IP-адресов.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.
'''
import subprocess
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import logging


logging.basicConfig(level=logging.INFO)


def ping_ip_addresses(ip_list):
    success_list = []
    fail_list = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        result = executor.map(ping, ip_list)
    for status in result:
        if status[1] == 0:
            success_list.append(status[0])
        else:
            fail_list.append(status[0])
    return tuple([success_list, fail_list])


def ping(ip):
    status = subprocess.call(["ping", ip, "-n", "1"], stdout=subprocess.PIPE)
    return (ip, status)


if __name__ == '__main__':
    list_ip = ['1.1.1', '8.8.8.8', '8.8.4.4', '8.8.7.1', '192.168.1.1', 'mail.ru', 'google.com','lalala']
    pprint(ping_ip_addresses(list_ip))
