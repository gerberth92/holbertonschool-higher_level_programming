#!/usr/bin/python3
"""
Este modulo se conecta con un servidor sql.
"""
import MySQLdb
from sys import argv


def main():
    """
    Este es el punto de entrada
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE 'N%'\
                ORDER BY id ASC")
    states = cur.fetchall()

    for estado in states:
        print(estado)

if __name__ == "__main__":
    main()
