#!/usr/bin/python
from __future__ import print_function
import sqlite3
import tkFileDialog, csv, sys

def main():

	# Get Name Database
	dbName = "C:\\Users\Trakansak-PC\Desktop\New folder\pythonsqlite.db"

	# Creating Table on Database
	tables = {}
	tables['Students'] = (
    "DROP TABLE Students ")
	tables['Student_Records'] = (
    "DROP TABLE Student_Records ")

	# Connect Database
	sqlite3_connection = sqlite3.connect(dbName)
	cursor = sqlite3_connection.cursor()
	
	# Alert Create Tables
	for name, ddl in tables.iteritems():
			print ("Deleting table {}: ".format(name), end='')
			cursor.execute(ddl)

	sqlite3_connection.commit()
	sqlite3_connection.close()

main()
