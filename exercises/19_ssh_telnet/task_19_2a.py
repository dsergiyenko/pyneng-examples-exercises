# -*- coding: utf-8 -*-
'''
Задание 19.2a

Скопировать функцию send_config_commands из задания 19.2 и добавить параметр verbose,
который контролирует будет ли выводится на стандартный поток вывода
информация о том к какому устройству выполняется подключение.

verbose - это параметр функции send_config_commands, не параметр ConnectHandler!

По умолчанию, результат должен выводиться.

Пример работы функции:

In [13]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...

In [14]: result = send_config_commands(r1, commands, verbose=False)

In [15]:

Скрипт должен отправлять список команд commands на все устройства из файла devices.yaml с помощью функции send_config_commands.
'''

from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko import ConnectHandler
import yaml

commands = [
    'logging 10.255.255.1', 'logging buffered 20010', 'no logging console'
]

def send_config_commands(device, config_commands, verbose=True):
    try:
        result=''
        if verbose == True:
            print ("connecting to "+ device['ip'])
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        result = net_connect.send_config_set(config_commands)
        net_connect.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(e)

    return result


if __name__ == '__main__':
    with open("devices.yaml") as devices_file:
        device = yaml.safe_load(devices_file)
    send_config_commands(device[0], commands,verbose=True)
