# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к одному устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает строку с выводом команды.

Скрипт должен отправлять команду command на все устройства из файла devices.yaml с помощью функции send_show_command.

'''
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko import ConnectHandler
import yaml

command = 'sh ip int br'

def send_show_command(device, command):
    try:
        output=''
        net_connect = ConnectHandler(**device)
        output = net_connect.send_command(command)
        print (output)
        net_connect.disconnect()
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        print(e)
    
    return output


if __name__ == '__main__':

    with open("devices.yaml") as devices_file:
        device = yaml.safe_load(devices_file)
    send_show_command(device[0], command)