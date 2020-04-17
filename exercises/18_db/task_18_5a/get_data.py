# -*- coding: utf-8 -*-
import sqlite3
import sys
from tabulate import tabulate

db_filename = 'dhcp_snooping.db'

if len(sys.argv) == 3:
    key, value = sys.argv[1:]
    keys = ['vlan', 'mac', 'ip', 'interface', 'switch']
    if not key in keys:
        print('Enter key from {}'.format(', '.join(keys)))
    else:
        conn = sqlite3.connect(db_filename)
        print('\nDetailed information for host(s) with', key, value)
        query = "select * from dhcp  where active = 1 and "+key+" = '"+value+"' "
        result = conn.execute(query)
        print('Active records: ')
        print(tabulate(result))
        query = "select * from dhcp  where active = 0 and "+key+" = '"+value+"' "
        result = conn.execute(query)
        print('Inactive records: ')
        print(tabulate(result))
elif len(sys.argv) == 1:
    conn = sqlite3.connect(db_filename)
    query = 'select * from dhcp' + ' where active = 1'
    result = conn.execute(query)
    print('Active records: ')
    print(tabulate(result))
    query = 'select * from dhcp' + ' where active = 0'
    result = conn.execute(query)
    print('Inactive records: ')
    print(tabulate(result))
else: 
    print("Please enter 2 or 0 arguments")
    exit()

