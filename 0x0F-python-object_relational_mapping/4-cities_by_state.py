#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    # inicializar cursor
    cur = db.cursor()

    # Query
    cur.execute("SELECT cities.id, cities.name, states.name \
                 FROM cities, states WHERE cities.state_id = states.id\
                 ORDER BY cities.id ASC")

    # Print
    for row in cur.fetchall():  # fetch (recuperar) trae la información
        print(row)

    # close cursor
    db.close()
