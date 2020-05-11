# -*- coding: utf-8 -*-
'''
Задание 19.2c

Скопировать функцию send_config_commands из задания 19.2b и переделать ее таким образом:

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды. Это значение по умолчанию, поэтому нажатие любой комбинации воспринимается как y
* n или no - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить работу функции можно на одном устройстве.

Пример работы функции:

In [11]: result = send_config_commands(r1, commands)
Подключаюсь к 192.168.100.1...
Команда "logging 0255.255.1" выполнилась с ошибкой "Invalid input detected at '^' marker." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: y
Команда "logging" выполнилась с ошибкой "Incomplete command." на устройстве 192.168.100.1
Продолжать выполнять команды? [y]/n: n

In [12]: pprint(result)
({},
 {'logging': 'config term\n'
             'Enter configuration commands, one per line.  End with CNTL/Z.\n'
             'R1(config)#logging\n'
             '% Incomplete command.\n'
             '\n'
             'R1(config)#',
  'logging 0255.255.1': 'config term\n'
                        'Enter configuration commands, one per line.  End with '
                        'CNTL/Z.\n'
                        'R1(config)#logging 0255.255.1\n'
                        '                   ^\n'
                        "% Invalid input detected at '^' marker.\n"
                        '\n'
                        'R1(config)#'})

'''

import re

# списки команд с ошибками и без:
commands_with_errors = ['logging 0255.255.1', 'logging', 'a']
correct_commands = ['logging buffered 20010', 'ip http server']

commands = commands_with_errors + correct_commands




from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko import ConnectHandler
import yaml
from pprint import pprint

def send_config_commands(device, config_commands, verbose=True):
    try:
        good={}
        bad={}
        result=''
        if verbose == True:
            print ("connecting to "+ device['ip'])
        net_connect = ConnectHandler(**device)
        net_connect.enable()
        net_connect.config_mode()
        for command in config_commands:
            result = net_connect.send_config_set(command)
            errors = re.findall(r'% (.+)', result)
            if errors:
                bad.update({command:result})
                print ('Команда "'+command+'" выполнилась с ошибкой "'+errors[0]+'" на устройстве '+device['ip'])
                answer = input('\nError occured, continue executing commands? [y]/n: ')
                if answer in ('n',):
                    break
            else:
                good.update({command:result})
        net_connect.exit_config_mode()
        net_connect.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(e)
    return (good, bad,)


if __name__ == '__main__':
    with open("devices.yaml") as devices_file:
        device = yaml.safe_load(devices_file)
    r = send_config_commands(device[0], commands,verbose=True)
    pprint (r)