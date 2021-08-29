import core.common.db_config as db


class AddressBook:
    def add(self, arg):
        """
        Створює новий запис в адресну книжку за вказаним іменем.
        :param request: dict - стрічка, де спочатку обов'язково йде ім'я, а потім одна або декілька інформацій в будь-якому порядку: адреса, номер тлф, email, день народження
        :return: str - виводить (повертає) стрічку з повідомленням користувачу, де каже, що все добре і все добавлено, або вказує, що є помилка і яка.
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
                    return f'For record {arg["name"]}, {fields[1]} is already exist. Please use "Change" function'
            else:

                add_record = (arg[fields[0]], arg[fields[1]])
                db.cur.execute(f"""INSERT INTO contacts(name, {fields[1]})
                    VALUES(?, ?);""", add_record)
                db.conn.commit()
                return 'Record added'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def change(self, arg):
        """
        Змінює запис за вказаним іменем в адресній книзі.
        :param request: dict - стрічка, де спочатку обов'язково йде ім'я, а потім нова інформація (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і змінено, або вказує, що є помилка і яка.
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
            print("Something went wrong", error)
        return f'{field} changed'

    def delete(self, arg):
        """
        Видаляє запис за вказаним іменем у адресній книзі. Акщо вхідна стрічка містить тільки ім'я, то видаляється все, що збережено за цим іменем.
        :param request: dict - стрічка, де спочатку обов'язково ім'я, а потім або інформація, яку треба видалити (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і видалено, або вказує, що є помилка і яка.
        """

        try:
            db.cur.execute("""DELETE FROM contacts
              WHERE name = ?""", (arg['name'],))
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        return f'Record {arg["name"]} deleted'

    def filter(self, arg):
        """
        Шукає інформацію в адресній книзі за співпадінням по введеній стрічці.
        :param request: dict - стрічка, за якою виконуємо пошук
        :return: str - повертає стрічку, де записана вся інформаційна лінія (імя, email, тлф, день народження), в якій було співпадіння. Якщо таких ліній декілька, то вони всі
        в стрічці розділені знаком \n. Якщо співпадіння немає, або помилка, то повертає стрічку-повідомлення про це.
        """
        result = ''

        try:
            db.cur.execute(
                """SELECT * FROM contacts WHERE name like ? OR phone like ? OR email like ? OR birthday like ?;""", ('%'+arg['phrase']+'%', '%'+arg['phrase']+'%', '%'+arg['phrase']+'%', '%'+arg['phrase']+'%'))
            for i in db.cur.fetchall():
                result += str(i) + '\n'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        if result == '':
            return 'No matches'
        else:
            return result

    def show_users_birthday(self, arg):
        """
        Знаходить користувачів, у яких день народження через задану кількість днів від поточної дати.: param days_number: - кількість днів, що додається до поточної дати.: return: - повертаємо стрічку з записом всіх імен користувачів ті їх днів народження, наприклад "ім'я: yyyy-mm-dd, \n ім'я: yyyy-mm-dd, \n...".
        """
        result = ''
        try:
            db.cur.execute(
                f"""SELECT name FROM contacts WHERE strftime('%j', birthday) = strftime('%j', (date('now','+{arg['days']} days'))) ;""")
            for i in db.cur.fetchall():
                result += str(i[0]) + '\n'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        if result == '':
            return 'No birthdays in this day'
        else:
            return result

    def get_records(self, arg):
        result = ''
        try:
            db.cur.execute(
                f"""SELECT * FROM contacts ;""")
            for i in db.cur.fetchall():
                result += str(i) + '\n'
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
        if result == '':
            return 'Address book is empty yet'
        else:
            return result
