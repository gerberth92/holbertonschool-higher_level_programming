#!/usr/bin/python3
"""
Este modulo se conecta con un servidor sql.
"""
import MySQLdb
from sys import argv


def main():
    """
    Este es el punto de entrada

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
        argv[4]: city name
    """
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name = '{}'\
                ORDER BY id ASC".format(argv[4]))
    states = cur.fetchall()

    for estado in states:
        print(estado)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
