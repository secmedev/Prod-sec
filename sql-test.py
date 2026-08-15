# semgrep-sql-test.py

import sqlite3

def get_user(username):
    conn = sqlite3.connect("test.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return conn.execute(query).fetchall()
