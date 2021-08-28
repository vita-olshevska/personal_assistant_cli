from typing import Union


class Identifier:
    @staticmethod
    def is_phone(input_data: str) -> bool:
        return False

    @staticmethod
    def is_email(input_data: str) -> bool:
        return "@" in input_data

    @staticmethod
    def is_birthday(input_data: str) -> (Union[str, None], Union[str, None]):
        if input_data.count("-") != 2:
            return False

        parts = input_data.split("-")
        if not parts[0].isnumeric() or len(parts[0]) != 4:
            return False

        if not parts[1].isnumeric() or len(parts[1]) != 2:
            return False

        if not parts[2].isnumeric() or len(parts[2]) != 2:
            return False

        return True

    def identify(self, input_data: str) -> str:
        if self.is_phone(input_data):
            return "phone"

        if self.is_email(input_data):
            return "email"

        if self.is_birthday(input_data):
            return "birthday"

        return "address"
