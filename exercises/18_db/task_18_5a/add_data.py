# -*- coding: utf-8 -*-


import os
import sqlite3
import re
import glob
from pprint import pprint
import yaml


query_write_into_dhcp_snooping_table = '''insert into dhcp (mac, ip, vlan, interface, switch, active, last_active) values (?, ?, ?, ?, ?, 1, datetime('now'))'''
query_set_active_0_dhcp_snooping_table = '''update dhcp set active = 0'''
query_write_into_switches_table = '''insert into switches (hostname, location) values (?, ?)'''
delete_old_rows = '''DELETE FROM dhcp WHERE last_active <= date('now','-7 day') '''
dhcp_snooping_files = glob.glob('*dhcp_snooping.txt')
dhcp_snooping_files_new = glob.glob(os.path.join('new_data','*dhcp_snooping.txt'))
db_filename = 'dhcp_snooping.db'
regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

def write_list_to_database(db_filename, query_line, list_of_tuples=[]):
    conn = sqlite3.connect(db_filename)
    if list_of_tuples != []:
        for row in list_of_tuples:
            try:
                with conn:
                    conn.execute(query_line, row)
                    conn.commit()
            except sqlite3.IntegrityError as e:
                print('During data insertion: '+str(row)+' Error occured: ', e)
                if len(row) > 2:
                    print( 'Updating row           '+str(row)+' in database dhcp')
                    conn.execute("update dhcp set ip = '"+row[1]+"', vlan = "+row[2]+", interface = '"+row[3]+"', switch ='"+row[4]+"', active = 1, last_active = datetime('now') where mac = '"+row[0]+"'")
                    conn.commit()         
    else:
        try:
            conn.execute(query_line)
            conn.commit()
        except sqlite3.IntegrityError as e:
                print('During data insertion:  Error occured: ', e)
    conn.close()

result = []
for filename in dhcp_snooping_files:
    switch_name = filename.split('_')[0]
    with open(filename) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result.append(match.groups()+(switch_name,))


result_new = []
for filename in dhcp_snooping_files_new:
    switch_name = filename.split('\\')[1].split('_')[0]
    with open(filename) as data:
        for line in data:
            match = regex.search(line)
            if match:
                result_new.append(match.groups()+(switch_name,))

result_yml = []
with open('switches.yml') as f:
    templates = yaml.safe_load(f)
for sw in templates['switches']:
    result_yml.append( (sw, templates['switches'][sw],) )


print('Adding data into table switches...')
write_list_to_database(db_filename, query_write_into_switches_table, result_yml)
print('Adding data into table dhcp...')
write_list_to_database(db_filename,  query_write_into_dhcp_snooping_table, result)
print('Update data in table dhcp...')
print('set active = 0 in table dhcp...')
write_list_to_database(db_filename,  query_set_active_0_dhcp_snooping_table)
print('Update data in table dhcp with new files...')
write_list_to_database(db_filename,  query_write_into_dhcp_snooping_table, result_new)
print('Deleting rows, which older than 7 days...')
write_list_to_database(db_filename, delete_old_rows )
