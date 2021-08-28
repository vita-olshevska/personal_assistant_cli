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
    Функция принимает введённую строку и проверяет является ли она
    телефонным номером. Критерии проверки:
    - проверка на соответствие формату 380ХХХХХХХХХ
    - проверка на наличие букв
    - проверка на количество цифр после исключения символов:
        - 10 цифр, допускается, проверяется префикс '0' и форматируется (прибавляется +38)
        - 11 - допускается, проверяется префикс '80' и форматируется (прибавляется +3)
        - 12 - допускается, проверяется префикс '380' и форматируется (прибавляется +)
        - <> цифр - не допускается.
    Возвращает кортеж с 2-мя элементами:
    - если номер в отформатированном виде удовлетворяет критериям проверки
    то кортеж вида ('380ХХХХХХХХХ', None)
    - если не удовлетворяет то вида (None, 'описание ошибки для юзера')
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

# mail_ex = [
#             'Ima.Fool@iana.org',
#             'Ima.Fool@iana.o',
#             '1Fool@iana.org',
#             'first_last@iana.org   ',
#             'first.middle.last@iana.or',
#             'a@test.com',
#             '   abc111@test.com.net',
#             'sdfhb34@skjfnv.tyu',
#             'kjbщтщдтю.шгри@gfh.com',
#             'sefbijsefnvbjsenfvb',
#             ]
#

def email_verify(email):
    """
    Функция принимает строку - email.
    Критерии проверки:
    - наличие в строке одного символа '@';
    - символы перед '@' не должны содержать пробелов и состоять только из букв
    английского алфавита, цифр и символов: '.', '_', длинной не менее 1 символа
    (исключая '.', '_')
    - символы после '@' не должны содержать пробелов и должы состоять только
    из букв английского алфавита и цифр, заканчиваться символом '.'
    - после символа '.' только буквы английского алфавита в количестве от 2 до 3.
    Возвращает кортеж с 2-мя элементами:
    - если email удовлетворяет критериям проверки то кортеж вида ('email', None)
    - если не удовлетворяет то вида (None, 'описание ошибки для юзера')
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
