class AddressBook:
    def add(self, request: dict) -> str:
        """
         Creates a new entry in the address book by the specified name.
        :param request: str - string, where first the
        name goes, and then one or more information in any order: address, phone number, email, birthday
        :return: str - returns a string with a message to the user, where he says that everything is fine and everything
         is added, or indicates that there is an error and what exactly.
        """

        pass

    def change(self, request: dict) -> str:
        """
        Змінює запис за вказаним іменем в адресній книзі.
        :param request: dict - стрічка, де спочатку обов'язково йде ім'я, а потім нова інформація (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і змінено, або вказує, що є помилка і яка.
        """
        pass

    def delete(self, request: dict) -> str:
        """
        Видаляє запис за вказаним іменем у адресній книзі. Акщо вхідна стрічка містить тільки ім'я, то видаляється все, що збережено за цим іменем.
        :param request: dict - стрічка, де спочатку обов'язково ім'я, а потім або інформація, яку треба видалити (адреса, номер тлф, email чи день народження)
        :return: str - повертає повідомлення користувачу, де каже, що все добре і видалено, або вказує, що є помилка і яка.
        """
        pass

    def filter(self, request: dict) -> str:
        """
        Шукає інформацію в адресній книзі за співпадінням по введеній стрічці.
        :param request: dict - стрічка, за якою виконуємо пошук
        :return: str - повертає стрічку, де записана вся інформаційна лінія (імя, email, тлф, день народження), в якій було співпадіння. Якщо таких ліній декілька, то вони всі
        в стрічці розділені знаком \n. Якщо співпадіння немає, або помилка, то повертає стрічку-повідомлення про це.
        """
        pass

    def show_users_birthday(self, request: dict) -> str:
        """
        Знаходить користувачів, у яких день народження через задану кількість днів від поточної дати.
        :param request: dict - кількість днів, що додається до поточної дати.
        :return:  - повертаємо стрічку з записом всіх імен користувачів ті їх днів народження, наприклад "ім'я: yyyy-mm-dd, \n ім'я: yyyy-mm-dd, \n...".
        """
        pass

    def get_records(self, request: dict) -> str:
        pass
