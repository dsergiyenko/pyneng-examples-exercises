# -*- coding: utf-8 -*-
'''
Задание 17.1

В этом задании нужно:
* взять содержимое нескольких файлов с выводом команды sh version
* распарсить вывод команды с помощью регулярных выражений и получить информацию об устройстве
* записать полученную информацию в файл в CSV формате

Для выполнения задания нужно создать две функции.

Функция parse_sh_version:
* ожидает как аргумент вывод команды sh version одной строкой (не имя файла)
* обрабатывает вывод, с помощью регулярных выражений
* возвращает кортеж из трёх элементов:
 * ios - в формате "12.4(5)T"
 * image - в формате "flash:c2800-advipservicesk9-mz.124-5.T.bin"
 * uptime - в формате "5 days, 3 hours, 3 minutes"

У функции write_inventory_to_csv должно быть два параметра:
 * data_filenames - ожидает как аргумент список имен файлов с выводом sh version
 * csv_filename - ожидает как аргумент имя файла (например, routers_inventory.csv), в который будет записана информация в формате CSV
* функция записывает содержимое в файл, в формате CSV и ничего не возвращает


Функция write_inventory_to_csv должна делать следующее:
* обработать информацию из каждого файла с выводом sh version:
 * sh_version_r1.txt, sh_version_r2.txt, sh_version_r3.txt
* с помощью функции parse_sh_version, из каждого вывода должна быть получена информация ios, image, uptime
* из имени файла нужно получить имя хоста
* после этого вся информация должна быть записана в CSV файл

В файле routers_inventory.csv должны быть такие столбцы:
* hostname, ios, image, uptime

В скрипте, с помощью модуля glob, создан список файлов, имя которых начинается на sh_vers.
Вы можете раскомментировать строку print(sh_version_files), чтобы посмотреть содержимое списка.

Кроме того, создан список заголовков (headers), который должен быть записан в CSV.


BOOTLDR: 7200 Software (C7200-KBOOT-M), Version 12.3(16), RELEASE SOFTWARE (fc4)
router uptime is 15 days, 8 hours, 32 minutes
System image file is "flash:c1841-advipservicesk9-mz.124-15.T1.bin"
'''

import glob
import re
import csv
from pprint import pprint

sh_version_files = glob.glob('sh_vers*')
#print(sh_version_files)

headers = ['hostname', 'ios', 'image', 'uptime']

def parse_sh_version(sh_ver_as_one_line):
    result = re.match(r'Cisco IOS Software.+?Version (\S+),.+?uptime is (.+minutes).+?image file is "(.+?)"', sh_ver_as_one_line, re.DOTALL)
    return (result.group(1), result.group(3), result.group(2))

result=[]
def write_inventory_to_csv(data_filenames_in, csv_filename_out):
    f_out = open(csv_filename_out, 'w', newline='')
    writer = csv.writer(f_out)
    writer.writerow(headers)
    for name in data_filenames_in:
        with open(name) as f:
            command_output = f.read()
            result = parse_sh_version(command_output)
            result_list = []
            result_list.append(name.split('_')[2].split('.')[0])
            for item in result: result_list.append(item)
            writer.writerow(result_list)


if __name__ == '__main__':
    write_inventory_to_csv(sh_version_files, 'sh_ver_out.csv')