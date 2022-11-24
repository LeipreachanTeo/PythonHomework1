import re


def find_contacts(query):
    query = ' '.join(query)
    with open('students.html') as file:
        for line in file:
            if query in line:
                print(line)


def add_contacts():
    with open('students.html', "a") as file:
        last_name = input("Введите фамилию: ").capitalize()
        name = input("Введите имя: ").capitalize()
        number_phone = input("Введите номер телефона: ")
        file.write(f'{last_name} {name} | {number_phone}\n')


def del_contacts(query):
    query = ' '.join(query)
    pattern = re.compile(re.escape(query))
    with open('students.html', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
            file.truncate()


def all_contacts():
    with open('students.html') as file:
        for line in file:
            print(line)
