from fuzzywuzzy import process
COMMANDS = ['show records', 'show notes', 'add record', 'add note', 'change record', 'add tag',
            'change note', 'delete record', 'delete note', 'search record', 'search note', 'show birthdays',
            'filter note', 'sort', 'help', 'off']
comm = input('>>>: ').lower()


def check_command(comm):
    check = process.extractOne(comm, COMMANDS)
    if 70 <= check[1] < 100:
        return f'Do you mean: {check[0]}'
    elif check[1] == 100:
        return True
    elif check[1] < 70:
        return 'Unknown command'
