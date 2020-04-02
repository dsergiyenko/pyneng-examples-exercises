# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

'''
import ipaddress


def convert_ranges_to_ip_list(ipaddress_list):
    return_list = []
    for addr in addresses:
        if len(addr.split('.')) == 4 and '-' in addr.split('.')[3]:
            range_start = int(addr.split('.')[3].split('-')[0])
            range_end = int(addr.split('.')[3].split('-')[1])
            for octet in range(range_start, range_end+1):
                return_list.append((".".join(addr.split('.')[:3])+str(octet)))
        elif len(addr.split('.')) > 4 and '-' in addr.split('.')[3]:
            start_ip = ipaddress.IPv4Address(addr.split('-')[0])
            end_ip = ipaddress.IPv4Address(addr.split('-')[1])
            for ip_int in range(int(start_ip), int(end_ip)+1):
                return_list.append(str(ipaddress.IPv4Address(ip_int)))
        else:
            return_list.append(addr)
    return return_list


if __name__ == '__main__':
    addresses = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    convert_ranges_to_ip_list(addresses)
