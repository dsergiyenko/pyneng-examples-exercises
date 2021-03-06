# -*- coding: utf-8 -*-
'''
Задание 19.1b

Скопировать функцию send_show_command из задания 19.1a и переделать ее таким образом,
чтобы обрабатывалось не только исключение, которое генерируется
при ошибке аутентификации на устройстве, но и исключение,
которое генерируется, когда IP-адрес устройства недоступен.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените IP-адрес на устройстве или в файле devices.yaml.
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