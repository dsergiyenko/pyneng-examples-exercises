# -*- coding: utf-8 -*-


import os
import sqlite3
import re
import glob
from pprint import pprint
import yaml


query_write_into_dhcp_snooping_table = '''insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'''
query_write_into_switches_table = '''insert into switches (hostname, location) values (?, ?)'''
dhcp_snooping_files = glob.glob('*dhcp_snooping.txt')
db_filename = 'dhcp_snooping.db'
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

def write_list_to_database(db_filename, list_of_tuples, query_line):
    conn = sqlite3.connect(db_filename)
    for row in list_of_tuples:
        try:
            with conn:
                conn.execute(query_line, row)
        except sqlite3.IntegrityError as e:
            print('During data insertion: '+str(row)+' Error occured: ', e)
    conn.close()

result = []
for filename in dhcp_snooping_files:
    switch_name = filename.split('_')[0]
    with open(filename) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result.append(match.groups()+(switch_name,))

result_yml = []
with open('switches.yml') as f:
    templates = yaml.safe_load(f)

for sw in templates['switches']:
    result_yml.append( (sw, templates['switches'][sw],) )

print('Adding data into table switches...')
write_list_to_database(db_filename, result_yml, query_write_into_switches_table)
print('Adding data into table dhcp...')
write_list_to_database(db_filename, result, query_write_into_dhcp_snooping_table)

