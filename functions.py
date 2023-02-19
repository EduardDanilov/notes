
import datetime
import csv
import os.path

timestamp = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

def find_id():
    rowcount = 0
    for row in open('notes.csv'):
        rowcount += 1
    return rowcount

def write_null_row():
    data = [['id', 'name', 'text', 'timestamp']]
    with open('notes.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)

def add_note():
    id = find_id()
    name = input('Введите имя заметки: ')
    text = input('Введите текст заметки: ')
    data = [[id, name, text, timestamp]]
    with open('notes.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)
    print('Заметка добавлена\n')

def read_all_notes():
    with open('notes.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(f'id: {row[0]} \nНазвание заметки: {row[1]} \nТекст: {row[2]} \nВремя: {row[3]}')

def notes_editor():
    note_to_change = input('Введи имя заметки, которую будешь редактировать: ')
    with open('notes.csv') as f:
        reader = csv.reader(f, delimiter=';')
        user_notes = []
        for row in reader:
            user_notes.append(row)
        for block in user_notes:
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
                
    
    with open('notes.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in user_notes:
            writer.writerow(row)


def check_notes_before_read():
    file_path = "./notes.csv"
    if os.path.exists(file_path) == True:
        read_all_notes()
    else: 
        print('\nERROR: Файл с заметками не найден. Добавьте новую заметку\n')

def check_notes_before_add():
    file_path = "./notes.csv"
    if os.path.exists(file_path) == True:
        add_note()
    else: 
        write_null_row()
        add_note()
