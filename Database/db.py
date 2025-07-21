import sqlite3

try:
    dbase = sqlite3.connect("student_records.db")

except:
    print("Connection Error")
