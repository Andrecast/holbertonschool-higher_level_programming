#!/usr/bin/python3
"""script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    # inicializar cursor
    cur = db.cursor()

    # Query
    cur.execute("SELECT * FROM states WHERE name like '{}' \
                    ORDER BY id ASC".format(sys.argv[4]))

    # Print
    for row in cur.fetchall():  # fetch (recuperar) trae la información
        if row[1] == sys.argv[4]:
            print(row)

    # close cursor
    db.close()
