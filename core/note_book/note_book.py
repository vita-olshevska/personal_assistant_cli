import core.common.db_config as db


class NoteBook:

    def add(self, note, name):
        add_note = (note, name)
        try:
            db.cur.execute("""INSERT INTO notes(note, name)
            VALUES(?, ?);""", add_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def change(self, note, name):
        update_note = (note, name)
        try:
            db.cur.execute("""UPDATE notes
              SET note = ?
              WHERE name = ?""", update_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def delete(self, name):
        try:
            db.cur.execute("""DELETE FROM notes
              WHERE name = ?""", (name,))
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def filter_for_tags(self, tag):
        try:
            db.cur.execute("""SELECT note FROM notes WHERE tag = ?;""", tag)
            print(db.cur.fetchall())
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def add_tag_to_note(self, tag, name):
        add_tag = (tag, name)
        try:
            db.cur.execute("""UPDATE notes
                SET tag = ?
                WHERE name = ?""", add_tag)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
