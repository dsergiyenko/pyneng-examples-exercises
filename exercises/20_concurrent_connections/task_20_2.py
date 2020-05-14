# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_show_command_to_devices, которая отправляет
одну и ту же команду show на разные устройства в параллельных потоках,
а затем записывает вывод команд в файл.

Параметры функции:
* devices - список словарей с параметрами подключения к устройствам
* command - команда
* filename - имя файла, в который будут записаны выводы всех команд
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция ничего не возвращает.

Вывод команд должен быть записан в файл в таком формате (перед выводом команды надо написать имя хоста и саму команду):

R1#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.1   YES NVRAM  up                    up
Ethernet0/1                192.168.200.1   YES NVRAM  up                    up
R2#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.2   YES NVRAM  up                    up
Ethernet0/1                10.1.1.1        YES NVRAM  administratively down down
R3#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
Ethernet0/0                192.168.100.3   YES NVRAM  up                    up
Ethernet0/1                unassigned      YES NVRAM  administratively down down

Для выполнения задания можно создавать любые дополнительные функции.

Проверить работу функции на устройствах из файла devices.yaml
'''

# -*- coding: utf-8 -*-

import yaml
from netmiko import (NetMikoAuthenticationException, NetMikoTimeoutException, ConnectHandler)
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

    

def connect_ssh(devices, command):
    result=''
    try:
        with ConnectHandler(**devices) as net_connect:
            net_connect.enable()
            hostname = net_connect.find_prompt()[:-1]
            result += hostname+'# '+command+'\n'
            print('Connection to device: '+hostname )
            result += net_connect.send_command(command)
            result += '\n'
            net_connect.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(e)
    return result

def send_show_command_to_devices(devices, command, filename, limit=3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(connect_ssh, devices, repeat(command) )
    with open(filename, 'w') as f:
        for i in f_result: f.write(i)


if __name__ == '__main__':
    with open("devices.yaml") as devices_file:
        devices = yaml.safe_load(devices_file)
        send_show_command_to_devices( devices, 'show int des', 'result.txt', 3)














