#!/usr/bin/python3
import MySQLdb
"""
Este modulo se conecta con un servidor sql.
"""


db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="hbtn_0e_0_usa", port="3306")

cur = db.cursor()
cur.execute("SELECT * FROM states")