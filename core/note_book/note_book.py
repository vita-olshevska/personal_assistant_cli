import core.common.db_config as db


class NoteBook:

    def add(self, arg):
        value = (arg['text'],)

        try:
            db.cur.execute("""INSERT INTO notes(note)
            VALUES(?);""", value)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        return 'Note saved'

    def change(self, arg):
        fields = list(arg.keys())
        update_note = (arg[fields[1]], arg[fields[0]])
        try:
            db.cur.execute(
                """UPDATE notes
                SET note = ?
                WHERE id = ?""", update_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        return 'Note edited'

    def delete(self, arg):
        try:
            db.cur.execute("""DELETE FROM notes
              WHERE id = ?""", (arg['id'],))
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        return 'Note deleted'

    def filter_for_tags(self, arg):
        result = ''
        try:
            db.cur.execute(
                """SELECT note FROM notes WHERE tag = ?;""", (arg['tag'],))
            for i in db.cur.fetchall():
                result += str(i[0]) + '\n'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        if result == '':
            return 'No matches'
        else:
            return result

    def add_tag_to_note(self, arg):
        fields = list(arg.keys())
        add_tag = (arg[fields[1]], arg[fields[0]])
        try:
            db.cur.execute("""UPDATE notes
                SET tag = ?
                WHERE id = ?""", add_tag)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong. Check your id", error)
        return 'Tag added'

    def search(self, arg):
        result = ''
        try:
            db.cur.execute(
                """SELECT * FROM notes WHERE note like ? ;""", ('%'+arg['phrase']+'%'))
            for i in db.cur.fetchall():
                result += str(i[0]) + '\n'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        if result == '':
            return 'No matches'
        else:
            return result

    def get_table(self, arg):
        try:
            db.cur.execute(
                """SELECT * FROM notes ;""")
            for i in db.cur.fetchall():
                print(i, end='\n')
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
