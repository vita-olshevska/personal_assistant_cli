import sqlite3
conn = sqlite3.connect('project.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   phone INTEGER,
   address TEXT,
   email TEXT,
   birthday TEXT);
""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS notes(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   tag TEXT,
   note TEXT);
""")
conn.commit()
