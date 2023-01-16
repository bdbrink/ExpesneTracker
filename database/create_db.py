#!/usr/bin/env python3

import sqlite3

conn = sqlite3.connect("expenses.db")

cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS expenses
        (id INTERGER PRIMARY KEY,
        Date DATE,
        description TEXT,
        category TEXT,
        price REAL)
""")

conn.commit()
conn.close()