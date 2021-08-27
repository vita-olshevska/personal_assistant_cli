from core.address_book.address_book import AddressBook
from core.note_book.note_book import NoteBook
from core.sort_manager.sort_manager import SortManager

import types


class ContextAnalyzer:
    """"""
    def analyze(self, request: str) -> (type, types.FunctionType, str):
        """
         Отримує стрічку-запит від користувача та повертає із цієї стрічки:
            - хто робить цю команду (AddressBook чи NoteBook).
            - команду
            - все інше, що після імені
        """
        responsible_module, command, user_data = None, None, None
        words = request.split()
        if request == "off":
            responsible_module = "main"
            command = "off"
        elif "sort" == words[0]:
            responsible_module = SortManager
            command = SortManager.sort
            user_data = " ".join(words[1:])
        elif "record" == words[1]:
            responsible_module = AddressBook
            if "add" == words[0]:
                command = AddressBook.add
            elif "change" == words[0]:
                command = AddressBook.change
            elif "delete" == words[0]:
                command = AddressBook.delete
            elif "filter" == words[0]:
                command = AddressBook.filter
            elif "show birthday" in request:
                # TODO: think about such case
                command = AddressBook.show_users_birthday

            user_data = " ".join(words[2:])
        elif "note" == words[1]:
            responsible_module = NoteBook
            if "add" == words[0]:
                command = NoteBook.add
            elif "change" == words[0]:
                command = NoteBook.change
            elif "delete" == words[0]:
                command = NoteBook.delete
            elif "filter" == words[0]:
                command = NoteBook.filter_for_tags
            elif "tag" == words[0]:
                command = NoteBook.add_tag_to_note

            user_data = " ".join(words[2:])

        return responsible_module, command, user_data
