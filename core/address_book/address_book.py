class AddressBook:
    def add(self, request: str) -> str:
        """
        Creates a new entry in the address book by the specified name.
        :param request: str - string, where first the
        name goes, and then one or more information in any order: address, phone number, email, birthday
        :return: str - returns a string with a message to the user, where he says that everything is fine and everything
         is added,
        or indicates that there is an error and what exactly.
        """
        pass

    def change(self, request: str) -> str:
        """
        Changes the record for the specified name in the address book.
        :param request: str - string, where first the name must be followed, and then new information (address, phone
        number, email or birthday)
        :return: str - returns a message to the user, where he says that everything is fine and changed, or indicates
        that there is an error and what.
        """
        pass

    def delete(self, request: str) -> str:
        """
        Deletes the record for the specified name in the address book. If the input tape contains only the name,
        everything saved by that name is deleted.
        :param request: str - a string where first the name is obligatory, and then or the information which needs to be
        deleted (address, phone number, email or birthday)
        :return: str - returns a message to the user, where he says that everything is fine and deleted, or indicates
        that there is an error and what.
        """
        pass

    def filter(self, request: str) -> str:
        """
        Searches for information in the address book by coincidence on the entered string.
        :param request: str - the string we are searching for
        :return: str - returns the string, which contains the entire information line (name, email, phone, birthday), in
        which there was a match. If there are several such lines, they are all separated in the string by a sign \n. If
        there is no match, or an error, it returns a message about it.
        """
        pass

    def show_users_birthday(self, days_number: int) -> str:
        """
        Finds users whose birthday is a specified number of days from the current date.
        :param days_number: the number of days added to the current date.
        :return:  returns a string with record of all names of users and their birthdays, for example "name: yyyy-mm-dd,
        \n name: yyyy-mm-dd, \n ...".
        """
        pass
