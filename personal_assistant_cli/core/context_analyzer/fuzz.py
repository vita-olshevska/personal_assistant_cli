from fuzzywuzzy import process
COMMANDS = ['show records', 'show notes', 'add record', 'add note', 'change record', 'add tag',
            'change note', 'delete record', 'delete note', 'search record', 'search note', 'show birthdays',
            'filter note', 'sort', 'help', 'off']


def check_command(comm):
    check = process.extractOne(comm, COMMANDS)
    if 70 <= check[1] < 100:
        choice = input(f'Maybe you mean: {check[0]}? Please, choose a number: 1 - yes, 2 - no: ')
        if choice == '1':
            return True, check[0]
        else:
            return True, comm
    elif check[1] == 100:
        return True, comm
    elif check[1] < 70:
        return False, 'Unknown command'
