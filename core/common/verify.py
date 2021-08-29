import re

def phone_verify(phone_num):
    """
    The function takes the input string and checks if it is phone number.
    Verification criteria:
    - check for compliance with the 380XXXXXXXXX format
    - checking for letters
    - check for the number of digits after excluding characters:
        - 10 digits, allowed, prefix '0' is checked and formatted (+38 is added)
        - 11 - allowed, prefix '80' is checked and formatted (+3 is added)
        - 12 - allowed, prefix '380' is checked and formatted (appended +)
        - <> digits - not allowed.
    Returns a tuple with 2 elements:
    - if the number in the formatted form meets the verification criteria
    then a tuple of the form ('380XXXXXXXXX', None)
    - if it does not satisfy that of the form (None, 'error description for
    the user')
    """
    # проверка на наличие букв - исключения
    if re.search(r'[a-zA-ZА-Яа-я]', phone_num) != None:
        return (None, 'Some letters in the entered number, and this is not in \
form, please enter in 38XXXXXXXXXX format')
    else:
        # удаление символов
        clean_phone_num = re.sub(r'\D', '', phone_num)
        # проверка количества цифр
        for i in range(10,13):
            preffix = '380'
            if len(clean_phone_num) == i:
                # проверка префикса номера
                if clean_phone_num.startswith(preffix[12 - i:len(preffix)]):
                # форматирование номера если удовлетворительное количество
                # цифр от 10 до 12
                    verifi_phone_num = preffix[0:(12 - i)] + clean_phone_num
                    return (verifi_phone_num, None)
                else:
                    return (None, 'Enter the number in 38XXXXXXXXXX format, please)')
            elif len(clean_phone_num) < 10 or len(clean_phone_num) > 12:
                return (None, 'The number of digits in the entered number is not in \
form, please enter in 38XXXXXXXXXX format')


def email_verify(email):
    """
The function accepts a string - email.
    Verification criteria:
    - the presence of one symbol '@';
    - characters before '@' must not contain spaces and only consist of letters
    Eng alphabet, numbers and symbols: '.', '_', at least 1 character long.
    - characters after '@' should not contain spaces and should only be
    from letters of the English alphabet and numbers, end with the character '.'
    - after the '.' only letters of the Eng alphabet in the amount from 2 to 3.
    Returns a tuple with 2 elements:
    - if the email meets the validation criteria, then a tuple of the form
    ('email', None)
    - if it does not satisfy that of the form (None, 'error description
    for the user')
    """
    # очистка пробелов вначале и в конце
    clean_email = email.strip()

    if re.fullmatch(r'[0-9a-zA-Z_.]+@[a-zA-Z]+[.][a-zA-Z]{2,3}', clean_email) == None:
        return (None, 'The text you entered is not an e-mail, please try again')
    else:
        return (clean_email, None)

def birthday_verify(birthday):
    """
    The function takes a string.
    Verification criteria:
    - format 'YYYY-MM-DD'
    - the number of months in a year is less than or equal to 12
    - the number of days is less than or equal to 31
     Returns a tuple with 2 elements:
     - if the date meets the verification criteria, then a tuple of the form ('YYYY-MM-DD', None)
    - if it does not satisfy that of the form (None, 'error description for the user')
    """
    clean_birthday = birthday.strip()
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', clean_birthday) == None:
        return (None, 'The text you entered is not a date in format YYYY-MM-DD, \
please try again')
    else:
        if int(clean_birthday.split('-')[1]) > 12:
            return (None, 'Only 12 months we have, or maby you from another planet? \
If it is true please contact with - www.nasa.gov)Or try again.')
        elif int(clean_birthday.split('-')[2]) > 31:
            return (None, 'There can be no more days in the month 31) Try again.')
        elif clean_birthday == '0000-00-00':
            return (clean_birthday, "You urgently need to listen to Weber's rock opera Jesus Christ - Superstar, 1971!!!!!")
        else:
            return(clean_birthday, None)
