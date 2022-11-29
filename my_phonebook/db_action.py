import os
# import pathlib
import random
from pathlib import Path
from random import randint
import menu
# import _drivers
# import pyodbc

# try:
#     con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=E:/Moi_Dokumenty/Practics/Python/HW_7/phonebook.accdb;'
#     conn = pyodbc.connect(con_string)
#     print("Connected To Database")
#
# except pyodbc.Error as e:
#     print("Error in Connection", e)


path = Path('phonebook.csv')
# path2 = Path('phonebook.accdb')


def counter_lines_csv():
    with open(path, 'r', encoding='utf-8') as f:
        return str(len(f.readlines()))

# def counter_lines_accdb():
#     with open(path2, 'r', encoding='utf-8') as f:
#         return str(len(f.readlines()))


def generate_fake_contact():
    print('*' * 35)
    print('\tГЕНЕРАЦИЯ КОНТАКТОВ ДЛЯ ОЗНАКОМЛЕНИЯ С ПРОГРАММОЙ')
    import datetime
    # dir_path = pathlib.Path.cwd()
    for _ in range(30):
        name = random.choice(open('E:/Moi_Dokumenty/Practics/Python/HW_7/my_phonebook/fake_data/names.txt', encoding='utf-8').readlines()).strip()
        surname = random.choice(open('E:/Moi_Dokumenty/Practics/Python/HW_7/my_phonebook/fake_data/surnames.txt', encoding='utf-8').readlines()).strip()
        birthday = datetime.date(randint(1950, 2000), randint(1, 12), randint(1, 28)).strftime("%d.%m.%Y")
        work = random.choice(open('E:/Moi_Dokumenty/Practics/Python/HW_7/my_phonebook/fake_data/companies.txt', encoding='utf-8').readlines()).strip()
        phonenum = '+' + str(random.randint(79000000000, 80000000000))
        u_data = [name, surname, birthday, work, phonenum]

        with open(path, 'a', encoding='utf-8') as f:
            line = ';'.join(u_data)
            f.write(counter_lines_csv() + ';' + line + '/n')

        # with open(path2, 'a', encoding='utf-8') as f:
        #     line = ';'.join(u_data)
        #     f.write(counter_lines_accdb() + ';' + line + '/n')

    print('Сгенерировано 30 фейковых аккаунтов.')


def add_new_contact():
    print('*' * 35)
    print('\tДОБАВЛЕНИЕ НОВОГО КОНТАКТА')
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    birthday = input('Дата рождения: ')
    work = input('Место работы: ')
    phonenum = input('Введите номер телефона. Если номеров несколько - разделяйте их запятыми: ')
    u_data = [name, surname, birthday, work, phonenum]

    with open(path, 'a', encoding='utf-8') as f:
        line = ';'.join(u_data)
        f.write(counter_lines_csv() + ';' + line + '/n')
        print('*' * 35)

    # with open(path2, 'a', encoding='utf-8') as f:
    #     line = ';'.join(u_data)
    #     f.write(counter_lines_accdb() + ';' + line + '/n')
    #     print('*' * 35)

    print('Новый контакт добавлен в справочник.')


def view_csv():
    print('*' * 35)
    if os.path.isfile(path):
        print('\tПРОСМОТР ВСЕХ КОНТАКТОВ')
        if int(counter_lines_csv()) < 2:
            print('В справочнике нет контактов.')
        else:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    print(line, end='')
    else:
        print('В справочнике нет контактов.')
        book_title()

# def view_accdb():
#     print('*' * 35)
#     if os.path.isfile(path):
#         print('\tПРОСМОТР ВСЕХ КОНТАКТОВ')
#         if int(counter_lines_accdb()) < 2:
#             print('В справочнике нет контактов.')
#         else:
#             with open(path2, 'r', encoding='utf-8') as f:
#                 for line in f:
#                     print(line, end='')
#     else:
#         print('В справочнике нет контактов.')
#         book_title()

def book_title():
    u_data = ['ID', 'ИМЯ', 'ФАМИЛИЯ', 'ДАТА РОЖДЕНИЯ', 'МЕСТО РАБОТЫ', 'НОМЕРА ТЕЛЕФОНОВ']
    with open(path, 'w', encoding='utf-8') as f:
        line = ';'.join(u_data)
        f.write(line + '/n')

    # with open(path2, 'w', encoding='utf-8') as f:
    #     line = ';'.join(u_data)
    #     f.write(line + '/n')


def delete_all():
    print('*' * 35)
    print('/tУДАЛЕНИЕ ВСЕХ КОНТАКТОВ')
    open(path, 'w', encoding='utf-8').close()
    open(path2, 'w', encoding='utf-8').close()
    book_title()
    print('Все контакты удалены.')
    yes_or_no = input('Если желаете добавить новый контакт - нажмите Enter.\n'
                      'Для возврата в меню введите любой символ и нажмите Enter: ')
    if yes_or_no == '':
        add_new_contact()
    else:
        menu.menu()
