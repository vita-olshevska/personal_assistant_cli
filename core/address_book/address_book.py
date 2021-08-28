from typing import Text
import db_config as db


class AddressBook:
    def add(self, name, phone, address, email, birthday):
        """
        Створює новий запис в адресну книжку за вказаним іменем.
        :param request: dict - стрічка, де спочатку обов'язково йде ім'я, а потім одна або декілька інформацій в будь-якому порядку: адреса, номер тлф, email, день народження
        :return: str - виводить (повертає) стрічку з повідомленням користувачу, де каже, що все добре і все добавлено, або вказує, що є помилка і яка.
        """

        add_record = (name, phone, address, email, birthday)
        try:
            db.cur.execute("""INSERT INTO contacts(name, phone, address, email, birthday)
        VALUES(?, ?, ?, ?, ?);""", add_record)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def change(self, name, value, field):
        """
        Змінює запис за вказаним іменем в адресній книзі.
        :param request: dict - стрічка, де спочатку обов'язково йде ім'я, а потім нова інформація (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і змінено, або вказує, що є помилка і яка.
        """
        update_note = (value, name)
        if field == 'name':
            sql = """UPDATE contacts
              SET name = ?
              WHERE name = ?"""
        elif field == 'phone':
            sql = """UPDATE contacts
              SET phone = ?
              WHERE name = ?"""
        elif field == 'address':
            sql = """UPDATE contacts
              SET address = ?
              WHERE name = ?"""
        elif field == 'email':
            sql = """UPDATE contacts
              SET email = ?
              WHERE name = ?"""
        elif field == 'birthday':
            sql = """UPDATE contacts
              SET birthday = ?
              WHERE name = ?"""
        try:
            db.cur.execute(sql, update_note)
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def delete(self, name: str) -> str:
        """
        Видаляє запис за вказаним іменем у адресній книзі. Акщо вхідна стрічка містить тільки ім'я, то видаляється все, що збережено за цим іменем.
        :param request: dict - стрічка, де спочатку обов'язково ім'я, а потім або інформація, яку треба видалити (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і видалено, або вказує, що є помилка і яка.
        """
        try:
            db.cur.execute("""DELETE FROM contacts
              WHERE name = ?""", (name,))
            db.conn.commit()
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def filter(self, request: dict) -> str:
        """
        Шукає інформацію в адресній книзі за співпадінням по введеній стрічці.
        :param request: dict - стрічка, за якою виконуємо пошук
        :return: str - повертає стрічку, де записана вся інформаційна лінія (імя, email, тлф, день народження), в якій було співпадіння. Якщо таких ліній декілька, то вони всі
        в стрічці розділені знаком \n. Якщо співпадіння немає, або помилка, то повертає стрічку-повідомлення про це.
        """
        try:
            db.cur.execute(
                """SELECT * FROM contacts WHERE name like ? OR phone like ? OR email like ? OR birthday like ?;""", ('%'+request+'%', '%'+request+'%', '%'+request+'%', '%'+request+'%'))
            for i in db.cur.fetchall():
                print(i, end='\n')
        except db.sqlite3.Error as error:
            print("Something went wrong", error)

    def show_users_birthday(self, interval):
        """
        Знаходить користувачів, у яких день народження через задану кількість днів від поточної дати.: param days_number: - кількість днів, що додається до поточної дати.: return: - повертаємо стрічку з записом всіх імен користувачів ті їх днів народження, наприклад "ім'я: yyyy-mm-dd, \n ім'я: yyyy-mm-dd, \n...".
        """
        try:
            db.cur.execute(
                f"""SELECT name FROM contacts WHERE strftime('%j', birthday) = strftime('%j', (date('now','+{interval} days'))) ;""")
            for i in db.cur.fetchall():
                print(i[0], end='\n')
        except db.sqlite3.Error as error:
            print("Something went wrong", error)
