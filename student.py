import sqlite3

def add_student(roll, name, s1, s2, s3):
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (?, ?, ?, ?, ?)", (roll, name, s1, s2, s3))
    conn.commit()
    conn.close()

def view_students():
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_student(roll):
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE roll=?", (roll,))
    row = cur.fetchone()
    conn.close()
    return row

def update_student(roll, name, s1, s2, s3):
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?, subject1=?, subject2=?, subject3=? WHERE roll=?",
                (name, s1, s2, s3, roll))
    conn.commit()
    conn.close()

def delete_student(roll):
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student WHERE roll=?", (roll,))
    conn.commit()
    conn.close()
