import sys
import functions

def main_menu():
    while True:
        print ('Меню: \n \
        1. Вывести все заметки (введи 1); \n \
        2. Добавить новую заметку (введи 2); \n \
        3. Редактировать заметку (введи 3); \n \
        4. Удалить заметку (введи 4). \n \
        Для выхода из приложения введи 0')
        user_number = input('Сделай выбор: ')
        if user_number == '1':
            functions.check_notes_before_read()
        elif user_number == '2':
            functions.check_notes_before_add()
        else: sys.exit()

main_menu()