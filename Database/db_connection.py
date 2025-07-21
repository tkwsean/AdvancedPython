import sqlite3

try:
    dbase = sqlite3.connect("student_records.db")
    print("Connected Successfully")
    dbase.execute(
        """CREATE TABLE students(ID INT PRIMARY KEY NOT NULL, NAMES TEXT NOT NULL, MARKS TEXT NOT NULL, GRADES TEXT NOT NULL)"""
    )
    dbase.close()
except:
    print("Connection Error")
