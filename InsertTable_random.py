#!/usr/bin/python
from __future__ import print_function
import sqlite3
import tkFileDialog, csv, sys
import names , random


def psql():
		
			# Get name Database
			dbName = "C:\\Users\Trakansak-PC\Desktop\New folder\pythonsqlite.db"

			# Get student detail
			studentId = random.randint(1000000000000, 9999999999999)
			studentFirstName =  names.get_first_name()
			studentLastName = names.get_last_name()
			letter = 'A','B','B+','C','C+','D+','D','F'

			
			# Get record from CSV file
			# csvfile = tkFileDialog.askopenfilename(title='Select CSV file',filetypes = [(("CSV files",".csv"),("all files","*.*"))])
			record = readCSV("C:\Users\Trakansak-PC\Desktop\Python_CSVtoDB_PG-master\data\Sarik.csv")
			

			# Connect to DB
			sqlite3_connection = sqlite3.connect(dbName)
			cursor = sqlite3_connection.cursor()

			# Insert Student Data
			cursor.execute("INSERT INTO Students (Student_id,First_name,Last_name)"
				"VALUES (?,?,?);", (studentId,studentFirstName,studentLastName))

			# Insert Transcript
			for term in record:
				for subject in term:
					try:
						cursor.execute(
							"INSERT INTO Student_Records "
							"(SubjectID,SubjectName,Weight,Section,Grade,Term,Student_id) "
							"VALUES (?,?,?,?,?,?,?);", 
							(subject[0], subject[1], subject[2], subject[3], random.choice(letter), 
							subject[5], studentId))
					except sqlite3.Error as error:
						print("Error: {}".format(error))

			# Check Status Completed
			print ("Complete")
			sqlite3_connection.commit()
			sqlite3_connection.close()


# Import File CSV
def readCSV(csvfile):
	with open(csvfile) as csvfile:
		next(csvfile)
		reader = csv.reader(csvfile)
		record, term = [], []
		for row in reader:			# add Subject to term
			term.append([row[0],row[1],row[2],row[3],row[4],row[5]])
			record.append(term)
			term = []
	return record

def main():
		x = 1
		while True:	
			try:
				psql()
			except Exception:
				pass

main()