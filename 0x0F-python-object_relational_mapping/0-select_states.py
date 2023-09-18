#!/usr/bin/python3
'''
List all states from
the `hbtn_0e_0_usa` database
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    '''
    Access data and fetch the state in the database
    '''
    db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            port=3306,
            passwd=argv[2],
            db=argv[3]
            )
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
