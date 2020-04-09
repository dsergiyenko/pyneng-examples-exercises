# -*- coding: utf-8 -*-
'''
Задание 17.2b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует draw_topology).

Проверить работу функции на файле topology.yaml. На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology.

Результат должен выглядеть так же, как схема в файле task_17_2b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''


import yaml
from pprint import pprint
from draw_network_graph import draw_topology


def transform_topology(yaml_file):
    with open(yaml_file) as f:
        d = yaml.safe_load(f)
    #pprint(d)
    list1=[]
    list2=[]
    for device in d.keys():
        for link in d[device]:
    #        print ({tuple([device, link]):  (list(d[device][link].items()))[0]})
            if tuple([device, link]) not in list2:
                list1.append( tuple([device, link]) )
                list2.append( (list(d[device][link].items()))[0])
    return dict(zip(list1, list2))


if __name__ == '__main__':
    draw_topology(transform_topology('topology.yaml'))