
import datetime
import csv
import os.path

timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def find_id():
    """Функция вычисления id"""
    rowcount = 0
    for row in open('notes.csv', encoding='utf-8-sig'): #Считает количество строк в файле с заметками
        rowcount += 1
    return rowcount


def write_null_row():
    """
    В случае, если файл с заметками отсутстует,
    эта функция создает его и добавляет заголовки столбцов
    """
    data = [['id', 'name', 'text', 'timestamp']]
    with open('notes.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)


def add_note():
    """Функция добавления заметки"""
    id = find_id()
    name = input('Введите имя заметки: ')
    text = input('Введите текст заметки: ')
    data = [[id, name, text, timestamp]]
    with open('notes.csv', 'a', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)
    print('Заметка добавлена\n')


def read_all_notes():
    """Функция вывода заметок"""
    with open('notes.csv', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(f'id: {row[0]} \nНазвание заметки: {row[1]} \nТекст: {row[2]} \nВремя: {row[3]}')


def notes_editor():
    """
    Функция редактирования заметки.
    Считывает построчно файл с заметками и формирует список для последующей обработки.
    """
    note_to_change = input('Введи имя заметки, которую будешь редактировать: ')
    with open('notes.csv', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        user_notes = [] #Новый список для дальнейшей обработки
        for row in reader:
            user_notes.append(row) #Считывает построчно файл с заметками и добавляет каждую строку как отдельный элемент списка в user_notes
        for block in user_notes: #В каждом элементе полученного списка ищет совпадение по имени заметки с тем, что ввел пользователь
            if block[1] == note_to_change:
                print('Что вы хотите изменить? \n \
Имя заметки (введи 1) \n \
Текст заметки (введи 2)')
                usr_choice = input('Введи значение: ')
                if usr_choice == '1':
                    block[1] = input('Введи новое имя для заметки: ')
                    block[3] = timestamp
                elif usr_choice == '2':
                    block[2] = input('Введи новый текст заметки: ')
                    block[3] = timestamp            
            # if note_to_change not in block[1]:
            #     print('Введено некорректное значение. Такой заметки не существует.')
                  
    with open('notes.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in user_notes:
            writer.writerow(row)


def delete_note():
    """
    Функция удаления заметок.
    Считывает построчно файл, добавляет строки в список для дальнейшей обраотки.
    Фильтрует получившийся список.
    В новый файл записывается список без выбранного пользователем элемента
    """
    note_for_delete = input('Введи имя заметки, которую будешь редактировать: ')
    with open('notes.csv', encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=';')
        worker_list = [] #Новый список для дальнейшей обработки
        list_for_writing = []
        for row in reader:
            worker_list.append(row) #Считывает построчно файл с заметками и добавляет каждую строку как отдельный элемент списка в worker_list
        for block in worker_list: #В каждом элементе полученного списка ищет совпадение по имени заметки с тем, что ввел пользователь
            if block[1] != note_for_delete:
                list_for_writing.append(block)

                  
    with open('notes.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in list_for_writing:
            writer.writerow(row)
    print('Заметка удалена\n')


def check_notes_before_read():
    """Проверяет, есть ли файл для чтения заметок"""
    file_path = "./notes.csv"
    if os.path.exists(file_path) == True:
        read_all_notes()
    else: 
        print('\nERROR: Файл с заметками не найден. Добавьте новую заметку, чтобы создать файл\n')


def check_notes_before_add():
    """Проверяет, есть ли файл для заметок.
    Если файл есть, то переходит к добавлению.
    Если файла нет, то вызывает функцию создания файла
    """
    file_path = "./notes.csv"
    if os.path.exists(file_path) == True:
        add_note()
    else: 
        write_null_row()
        add_note()
