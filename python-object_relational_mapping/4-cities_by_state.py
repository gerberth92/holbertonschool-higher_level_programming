#!/usr/bin/python3
"""
Este modulo incia la coneccion a un servidor sql
"""
from sys import argv
import MySQLdb


def main():
    """
    Este es el punto de entrada.

    Arguments:
        argv[1]: mysql username
        argv[2]: mysql password
        argv[3]: database name
    """
    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    
    cur = db.cursor()
    cur.execute("SELECT * FROM cities")

    cities = cur.fetchall()

    for resgistro in cities:
        print(resgistro)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()