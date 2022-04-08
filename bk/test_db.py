import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS products (
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [name] TEXT NOT NULL)
    """)

c.execute("""CREATE TABLE IF NOT EXISTS prices (
    [id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [price] INTEGER NOT NULL)
    """)

conn.commit()