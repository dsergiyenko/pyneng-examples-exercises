# -*- coding: utf-8 -*-
import sqlite3
import sys
from tabulate import tabulate

db_filename = 'dhcp_snooping.db'

query_dict = {
    'vlan': 'select mac, ip, interface, switch from dhcp where vlan = ?',
    'mac': 'select vlan, ip, interface, switch from dhcp where mac = ?',
    'ip': 'select vlan, mac, interface, switch from dhcp where ip = ?',
    'interface': 'select vlan, mac, ip, switch from dhcp where interface = ?',
    'switch': 'select vlan, mac, ip, interface from dhcp where switch = ?'
}

if len(sys.argv) == 3:
    key, value = sys.argv[1:]
    keys = query_dict.keys()
    if not key in keys:
        print('Enter key from {}'.format(', '.join(keys)))
    else:
        conn = sqlite3.connect(db_filename)
#        conn.row_factory = sqlite3.Row

        print('\nDetailed information for host(s) with', key, value)
        query = query_dict[key]
        result = conn.execute(query, (value, ))
        print(tabulate(result))
elif len(sys.argv) == 1:
    conn = sqlite3.connect(db_filename)
    query = 'select * from dhcp'
    result = conn.execute(query)
    print(tabulate(result))
else: 
    print("Please enter 2 or 0 arguments")
    exit()

