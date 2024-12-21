import sqlite3

# Establish a database connection and create a cursor
conn = sqlite3.connect("students.sqlite")
cursor = conn.cursor()

# Create the students table
sql_query = """
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    gender TEXT NOT NULL,
    age TEXT
)
"""
cursor.execute(sql_query)
