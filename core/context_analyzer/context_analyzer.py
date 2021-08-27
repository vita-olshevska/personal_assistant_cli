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
        pass
