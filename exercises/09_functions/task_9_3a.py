# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
def get_int_vlan_map(config_filename):
    access_dict = {}
    trunk_dict = {}
    interface = ''
    vlan = ''
    vlan_list = []
    with open(config_filename, 'r') as f:
        for line in f:
            if line.startswith('interface'):
                if interface != '':
                    access_dict.update({interface: '1'})
                    interface=''
                interface = line.split()[1].rstrip()
            if 'switchport access vlan' in line:
                vlan = line.split()[3].rstrip()
                access_dict.update({interface: vlan})
                interface = ''
                vlan = ''
                vlan_list = []
            elif 'switchport trunk allowed vlan' in line:
                vlan_list = line.split()[4].rstrip().split(',')
                trunk_dict.update({interface: vlan_list})
                interface = ''
                vlan = ''
                vlan_list = []
    data=tuple() 
    data=(access_dict, trunk_dict)  
    return data


get_int_vlan_map('config_sw2.txt')