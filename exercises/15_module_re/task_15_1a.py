# -*- coding: utf-8 -*-
'''
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.
interface Ethernet0/3
'''
import re
from pprint import pprint

#checked in windows
def get_ip_from_cfg(filename):
	result_dict={}
	config = open(filename).read()
	result = re.findall(r'interface (.+)(.*\n){0,3} ip address (\d+.\d+.\d+.\d+) (\d+.\d+.\d+.\d+)', config)
	if result:
		for interface, trash, ip, mask in result:
			result_dict.update({interface:(ip,mask)})
	return result_dict


if __name__ == '__main__':
    pprint( get_ip_from_cfg('config_r1.txt') )