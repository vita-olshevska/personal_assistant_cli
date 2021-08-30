import core.common.db_config as db


class AddressBook:
    def add(self, arg):
        """
        Creates a new record in the address book by the specified name.
        :param request: dict - dictionary, where first the name goes, and then one or more information in any order: address, phone number, email, birthday (e.g. {‘name’: ‘John’, ‘email’: john@gmail.com})
        :return: str - returns a string with a message to the user, whether everything is fine and everything is added, or indicates that there is an error and what exactly.
        """

        fields = list(arg.keys())
        try:
            db.cur.execute(
                """SELECT count(*) FROM contacts WHERE name = ?;""", (arg['name'],))
            all_results = db.cur.fetchall()
            if all_results[0][0] == 1:
                db.cur.execute(
                    f"""SELECT {fields[1]} FROM contacts WHERE name = ?;""", (arg['name'],))
                all_results = db.cur.fetchall()
                if all_results[0][0] == None:
                    AddressBook.change(self, arg)
                    return f'{fields[1]} changed'
                else:
                    return f'For record {arg["name"]}, {fields[1]} is already exist. Please use the next command: "change"'
            else:

                add_record = (arg[fields[0]], arg[fields[1]])
                db.cur.execute(f"""INSERT INTO contacts(name, {fields[1]})
                    VALUES(?, ?);""", add_record)
                db.conn.commit()
                return 'Record added'
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"

    def change(self, arg):
        """
        Changes the record for the specified name in the address book.
        :param request: dict - dictionary, where first the name must be followed, and then new information (address, phone number, email or birthday)
        :return: str - returns a message to the user, whether everything is fine and changed, or indicates that there is an error and what.
        """

        try:
            for key in arg.keys():
                if key != "name":
                    update_note = (arg[key], arg["name"])
                    sql = f"""UPDATE contacts
                    SET {key} = ?
                    WHERE name = ?"""
                    field = key
            db.cur.execute(sql, update_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"
        return f'{field} changed'

    def delete(self, arg):
        """
        Deletes the record for the specified name in the address book.
        :param request: dict - a dictionary containing the name for which you want to delete the record (e.g. {‘name’: ‘John’})
        :return: str - returns a message to the user, whether everything is fine and deleted, or indicates that there is an error and what.
        """

        try:
            db.cur.execute("""DELETE FROM contacts
              WHERE name = ?""", (arg['name'],))
            db.conn.commit()
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"
        return f'Record {arg["name"]} deleted'

    def filter(self, arg):
        """
        Searches for information in the address book by coincidence on the entered string.
        :param request: dict - the dictionary with the value we are searching for (e.g. {‘phrase’: ‘John’})
        :return: str - returns the string, which contains the entire information line (name, email, phone, birthday), in which there was a match. If there are several such lines, they are all separated in the string by a sign \n. If there is no match, or an error, it returns a message about it.
        """
        result = ''
        try:
            db.cur.execute(
                """SELECT * FROM contacts WHERE name like ? OR phone like ? OR email like ? OR birthday like ?;""", ('%'+arg['phrase']+'%', '%'+arg['phrase']+'%', '%'+arg['phrase']+'%', '%'+arg['phrase']+'%'))
            response = db.cur.fetchall()
            if len(response) > 0:
                result += "Name Phone Address Email Birthday\n"
                for i in response:
                    result += f"{i[1]} {i[2]} {i[3]} {i[4]} {i[5]}\n"
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"
        if result == '':
            return 'No matches'
        else:
            return result

    def show_users_birthday(self, arg):
        """
        Finds users whose birthday is a specified number of days from the current date.
        :param days_number: dict - the number of days (type: int) added to the current date (e.g. {‘days’, 36}).
        :return:  returns a string with all names of users and their birthdays, for example "name: yyyy-mm-dd, \n name: yyyy-mm-dd, \n ...".
        """
        result = ''
        try:
            db.cur.execute(
                f"""SELECT name, birthday FROM contacts WHERE strftime('%j', birthday) = strftime('%j', (date('now','+{arg['days']} days'))) ;""")
            for i in db.cur.fetchall():
                result += str(i[0]) + ': ' + str(i[1]) + '\n'
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"
        if result == '':
            return 'No birthdays in this day'
        else:
            return result

    def get_records(self, arg):
        result = ''
        try:
            db.cur.execute(
                f"""SELECT * FROM contacts ;""")
            response = db.cur.fetchall()
            if len(response) > 0:
                result += "Name Phone Address Email Birthday\n"
                for i in response:
                    result += f"{i[1]} {i[2]} {i[3]} {i[4]} {i[5]}\n"
        except db.sqlite3.Error as error:
            return f"Something went wrong, {error}"
        if result == '':
            return 'Address book is empty yet'
        else:
            return result
