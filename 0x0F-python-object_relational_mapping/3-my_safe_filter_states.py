#!/usr/bin/python3
"""A query that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    # inicializar cursor
    cur = db.cursor()

    # Query
    cur.execute("SELECT * FROM states WHERE name=%s", (sys.argv[4], ))

    # Print
    for row in cur.fetchall():  # fetch (recuperar) trae la información
        if row[1] == sys.argv[4]:
            print(row)

    # close cursor
    db.close()
