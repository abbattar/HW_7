import db_action as dba
import sys


def menu():
    choice = str(input(
        f'{"*" * 50}\n'
        '\t\tСПИСОК ДЕЙСТВИЙ:\n'
        '\t1. Показать все контакты\n'
        '\t2. Сгенерировать контакты\n'
        '\t3. Добавить контакт\n'
        '\t4. Удалить все контакты\n'
        '\t5. Закрыть программу\n'
        f'{"*" * 50}\n'
        '\tВведите номер действия и нажмите Enter: '))
    # match choise:
    #    case '1': 
    if choice == '1':
        dba.view_csv()
        # case '2':
    elif choice == '2':
        dba.generate_fake_contact()
        # case '3':
    elif choice == '3':
        dba.add_new_contact()
        # case '4':
    elif choice == '4':
        dba.delete_all()
        # case '5':
    elif choice == '5':
        sys.exit('Программа закрыта. Всего доброго!')
        # case _:
    else:
        print('Что-то пошло не так. Повторите ввод!')
