from core.address_book.address_book import AddressBook
from core.address_book.address_book_input_provider import AddressBookInputProvider

from core.note_book.note_book import NoteBook
from core.note_book.note_book_input_provider import NoteBookInputProvider

from core.sort_manager.sort_manager import SortManager
from core.context_analyzer.context_analyzer import ContextAnalyzer

if __name__ == "__main__":
    address_book = AddressBook()
    address_book_input_provider = AddressBookInputProvider()

    note_book = NoteBook()
    note_book_input_provider = NoteBookInputProvider()

    sort_manager = SortManager()
    context_analyzer = ContextAnalyzer()

    while True:
        user_request = input(">>> : ")
        responsible_module, command, user_data = context_analyzer.analyze(user_request)
        if responsible_module == AddressBook:
            if command:
                parsed_user_data = address_book_input_provider.provide(command, user_data)
                if "error" in parsed_user_data:
                    answer = parsed_user_data["error"]
                else:
                    answer = command(address_book, parsed_user_data)
            else:
                answer = "Wrong command for AddressBook module."
        elif responsible_module == NoteBook:
            if command:
                parsed_user_data = note_book_input_provider.provide(command, user_data)
                if "error" in parsed_user_data:
                    answer = parsed_user_data["error"]
                else:
                    answer = command(note_book, parsed_user_data)
            else:
                answer = "Wrong command for NoteBook module."
        elif responsible_module == SortManager:
            if command:
                answer = command(sort_manager, user_data)
            else:
                answer = "Wrong command for SortManager module."
        elif responsible_module == "main":
            if command == "off":
                print("Good bye!")
                break
            else:
                answer = "Wrong command for Main module."
        else:
            answer = "Can not understand what you mean."

        print(answer)






