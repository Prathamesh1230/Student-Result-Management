import sqlite3

def connect():
    conn = sqlite3.connect("results.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            subject1 INTEGER,
            subject2 INTEGER,
            subject3 INTEGER
        )
    """)
    conn.commit()
    conn.close()
