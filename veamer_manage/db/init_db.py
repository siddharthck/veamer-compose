import sqlite3, csv 
import os


def create_table(conn):
	conn.execute("CREATE TABLE MOVIES(ID INTEGER NOT NULL PRIMARY KEY,NAME TEXT NOT NULL ,DESCRIPTION TEXT ,CAST TEXT, YEAR INTEGER, DURATION_IN_MIN INTEGER )")
	conn.commit()



try:
	conn= sqlite3.connect("movies.db")
	create_table(conn)
	conn.close()

except:
	print("exception occured while connecting to db")





