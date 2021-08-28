from core.address_book.address_book import AddressBook
from core.common.identifier import Identifier

from types import FunctionType
from typing import Union


class AddressBookInputProvider:
    def __init__(self):
        self.__identifier = Identifier()
        self.__information_type = {"1": "phone", "2": "email", "3": "birthday", "4": "address"}

    def provide(self, command: Union[FunctionType, None], user_data: str) -> dict:
        if user_data is None or user_data == "":
            return self.__parse_user_data_with_requests(command)
        else:
            return self.__parse_user_data_from_scratch(user_data, command)

    ###############
    # Smart non-request bot:
    ###############

    def __parse_user_data_from_scratch(self, user_data: str, command: Union[FunctionType, None]) -> dict:
        if command == AddressBook.add:
            return self.__parse_add_user_data(user_data)
        elif command == AddressBook.change:
            return self.__parse_change_user_data(user_data)
        elif command == AddressBook.delete:
            return self.__parse_delete_user_data(user_data)
        elif command == AddressBook.filter:
            return self.__parse_filter_user_data(user_data)
        elif command == AddressBook.show_users_birthday:
            return self.__parse_show_birthdays_user_data(user_data)
        elif command == AddressBook.get_records:
            return {}
        else:
            return {"error": "Undefined command provided for AddressBook."}

    def __parse_add_user_data(self, user_data: str) -> dict:
        parsed_user_data = dict()
        parts = user_data.split()
        parsed_user_data["name"] = parts[0]

        address = ""
        for part in parts[1:]:
            if self.__identifier.is_email(part):
                parsed_user_data["email"] = part
            elif self.__identifier.is_phone(part):
                parsed_user_data["phone"] = part
            elif self.__identifier.is_birthday(part):
                parsed_user_data["birthday"] = part
            else:
                address += part + " "

        if address != "":
            parsed_user_data["address"] = address

        return parsed_user_data

    def __parse_change_user_data(self, user_data: str) -> dict:
        parsed_user_data = dict()
        parts = user_data.split()
        parsed_user_data["name"] = parts[0]

        address = ""
        for part in parts[1:]:
            if self.__identifier.is_email(part):
                parsed_user_data["email"] = part
            elif self.__identifier.is_phone(part):
                parsed_user_data["phone"] = part
            elif self.__identifier.is_birthday(part):
                parsed_user_data["birthday"] = part
            else:
                address += part + " "

        if address != "":
            parsed_user_data["address"] = address

        return parsed_user_data

    @staticmethod
    def __parse_delete_user_data(user_data: str) -> dict:
        return {"name": user_data}

    @staticmethod
    def __parse_filter_user_data(user_data: str) -> dict:
        return {"phrase": user_data}

    @staticmethod
    def __parse_show_birthdays_user_data(user_data: str) -> dict:
        if user_data.isnumeric():
            return {"days": int(user_data)}

        return {"error": f"User provide invalid number of days in show birthdays method: {user_data}"}

    ###############
    # Noising asking bot:
    ###############

    def __parse_user_data_with_requests(self, command: Union[FunctionType, None]) -> dict:
        if command == AddressBook.add:
            return self.__parse_add_with_requests()
        elif command == AddressBook.change:
            return self.__parse_change_with_requests()
        elif command == AddressBook.delete:
            return self.__parse_delete_with_requests()
        elif command == AddressBook.filter:
            return self.__parse_filter_with_requests()
        elif command == AddressBook.show_users_birthday:
            return self.__parse_show_birthdays_with_requests()
        elif command == AddressBook.get_records:
            return {}
        else:
            return {"error": "Undefined command provided for AddressBook."}

    def __parse_add_with_requests(self) -> dict:
        name = input("Please input a name: ")
        choice = input("Choose a number: 1 - Phone, 2 - Email, 3 - Birthday, 4 - Address ")
        if choice not in self.__information_type:
            return {"error": f"Wrong number: {choice}"}

        information = input("Input information: ")
        return {"name": name, self.__information_type[choice]: information}

    def __parse_change_with_requests(self) -> dict:
        name = input("Please input a name: ")
        choice = input("Choose a number: 1 - Phone, 2 - Email, 3 - Birthday, 4 - Address ")
        if choice not in self.__information_type:
            return {"error": f"Wrong number: {choice}"}

        information = input("Input information: ")
        return {"name": name, self.__information_type[choice]: information}

    @staticmethod
    def __parse_delete_with_requests() -> dict:
        name = input("Please input a name: ")

        return {"name": name}

    @staticmethod
    def __parse_filter_with_requests() -> dict:
        phrase = input("Please input searching phrase: ")

        return {"phrase": phrase}

    @staticmethod
    def __parse_show_birthdays_with_requests() -> dict:
        number_of_days = input("Please input a number of days: ")
        if number_of_days.isnumeric():
            return {"days": int(number_of_days)}

        return {"error": f"User provide invalid number of days in show birthdays method: {number_of_days}"}
