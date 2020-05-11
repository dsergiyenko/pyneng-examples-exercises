# -*- coding: utf-8 -*-
'''
Задание 19.1a

Скопировать функцию send_show_command из задания 19.1 и переделать ее таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, на стандартный поток вывода должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
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