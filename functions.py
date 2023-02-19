
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
    data = [[id, text, name, timestamp]]
    with open('notes.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=';')
        for row in data:
            writer.writerow(row)
    print('Заметка добавлена\n')

def read_all_notes():
    with open ('notes.csv', encoding='utf-8') as f:
        print(f.read())

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
