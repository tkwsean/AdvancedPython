import sqlite3

try:
    dbase = sqlite3.connect("student_records.db")
    print("Connected Successfully")
    cursor = dbase.cursor()
    cursor.execute(
        """INSERT INTO STUDENTS(ID, NAMES, MARKS, GRADES) VALUES (?, ?, ?, ?)""",
        (1, "Sean", "95", "A"),
    )
    dbase.commit()
    dbase.close()
except:
    print("Connection Error")
