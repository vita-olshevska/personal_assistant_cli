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
   note TEXT,
   name TEXT);
""")
conn.commit()

# cur.execute("""INSERT INTO contacts(id, name, phone, email, birthday)
#   VALUES('00001', 'Test', '380671232233', 'next@email.com', '1988-09-07');""")
# conn.commit()
#
# cur.execute("""INSERT INTO notes(id, tag, note, name)
#   VALUES('00001', '#first', 'some text', 'Alex');""")
# conn.commit()

# cur.execute(
#     """SELECT * FROM contacts;""")
# all_results = cur.fetchall()
# for i in all_results:
#     print(i, end='\n')
