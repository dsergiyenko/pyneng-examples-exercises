# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('ospf.txt', 'r') as f:
    for ospf_route in f:
        ospf_route=ospf_route.replace(',', '')
        ospf_route=ospf_route.replace('[', '')
        ospf_route=ospf_route.replace(']', '')
        netw = ospf_route.split()
        print('')
        print("{:23} {:23}".format('Protocol:', 'OSPF'))
        print("{:23} {:23}".format('Prefix:', netw[1] ))
        print("{:23} {:23}".format('AD/Metric:', netw[2]))
        print("{:23} {:23}".format('Next-Hop:', netw[4]))
        print("{:23} {:23}".format('Last update:', netw[5]))
        print("{:23} {:23}".format('Outbound Interface:', netw[6]))