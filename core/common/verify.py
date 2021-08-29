# тут написаны функции верификации телефонных номеров и email
import re

# примеры нломеров в списке
# phone_list = [
#             '234556',
#             '   i87ваи6796вкаи876',
#             '657483 6720267bh725294',
#             '+380665674521',
#             '  80970005647',
#             '+380667  778889',
#             '1010101010',
#             '11111111111',
#             '121212121212',
#             '0978884567',
#             '80667775566',
#             '380630051810',
#             ''
#             ]

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


# for i in phone_list:
#     print(phone_verify(i))

mail_ex = [
            'Ima.Fool@iana.org',
            'Ima.Fool@iana.o',
            '1Fool@iana.org',
            'first_last@iana.org   ',
            'first.middle.last@iana.or',
            'a@test.com',
            '   abc111@test.com.net',
            'sdfhb34@skjfnv.tyu',
            'kjbщтщдтю.шгри@gfh.com',
            'sefbijsefnvbjsenfvb',
            '.@ggg.cok'
            ]


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

    # if re.search(r'@',clean_email) == None:
    if re.fullmatch(r'[0-9a-zA-Z_.]+@+[a-zA-Z]+[.]+[a-zA-Z]{2,3}', clean_email) == None:
        return (None, 'The text you entered is not an e-mail, please try again')
    else:
        return (clean_email, None)

for i in mail_ex:
    print(email_verify(i))

date_list = [
            '2013-05-13',
            'dsfg-se-fb',
            '13-05-2022',
            '1235+23=34'
            ]
def birthday_verify(birthday):
    """

    """
    clean_birthday = birthday.strip()
    if re.fullmatch(r'\d{4}-\d{2}-\d{2}', clean_birthday) == None:
        return (None, 'The text you entered is not a date in format YYYY-MM-DD, \
please try again')
    else:
        return(clean_birthday, None)


# for i in date_list:
#     print(birthday_verify(i))
