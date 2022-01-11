#!/usr/bin/python3

import sqlite3
conn = sqlite3.connect("ndb.db")


param = str(input("ingrese el patron: "))


cursor = conn.cursor()

cursor.execute("select * from weas where weacont like ?",['%'+param+'%'])


res = cursor.fetchall()

for row in res:
    print(row)

