import sqlite3

try:
    dbase = sqlite3.connect("student_records.db")
    print("Connected Successfully")
    cursor = dbase.cursor()
    query = """SELECT * FROM STUDENTS"""
    cursor.execute(query)
    print(cursor.fetchall())  # Selects all the remaining rows after the previous query
    print(cursor.fetchone())  # Selects the next row
    print(cursor.fetchmany())  # Selects the N remaining rows after the previous query
    dbase.commit()
    dbase.close()
except:
    print("Connection Error")
