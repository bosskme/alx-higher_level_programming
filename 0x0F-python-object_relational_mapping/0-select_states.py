#!/usr/bin/python3
# List all states from hbtn_0e_0_usa database
import sys
import MySQLdb

if __name__== "__main__";
db = MySQL.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM 'states'")
[print(state) for statr in c.fetchall()]
