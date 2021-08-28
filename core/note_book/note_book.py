import core.common.db_config as db


class NoteBook:

    def add(self, note: str, name: str):
        add_note = (note, name)
        try:
            db.cur.execute("""INSERT INTO notes(note, name)
            VALUES(?, ?);""", add_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def change(self, note: str, id: int):
        update_note = (note, id)
        try:
            db.cur.execute("""UPDATE notes
              SET note = ?
              WHERE id = ?""", update_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def delete(self, id: int):
        try:
            db.cur.execute("""DELETE FROM notes
              WHERE id = ?""", (id,))
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def filter_for_tags(self, tag: str):
        try:
            db.cur.execute("""SELECT note FROM notes WHERE tag = ?;""", tag)
            print(db.cur.fetchall())
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def add_tag_to_note(self, tag: str, id: int):
        add_tag = (tag, id)
        try:
            db.cur.execute("""UPDATE notes
                SET tag = ?
                WHERE id = ?""", add_tag)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong. Check your id", error)

    def search(self, key: str):
        try:
            db.cur.execute(
                """SELECT * FROM notes WHERE note like ? ;""", ('%'+key+'%'))
            for i in db.cur.fetchall():
                print(i, end='\n')
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
