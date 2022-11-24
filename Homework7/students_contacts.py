import re


def find_students(query):
    query = ' '.join(query)
    with open('students.txt') as file:
        for line in file:
            if query in line:
                print(line)


def add_students():
    with open('students.txt', "a") as file:
        last_name = input("Введите фамилию: ").capitalize()
        first_name = input("Введите имя: ").capitalize()
        patronymic = input("Введите отчество: ").capitalize()
        number_class = input("Введите номер класса: ")
        age = input("Введите дату рождения")
        average_mark = input("Введите средний бал")
        file.write(f'{last_name} {first_name} {patronymic} {age} {number_class} {average_mark}\n')


def del_students(query):
    query = ' '.join(query)
    pattern = re.compile(re.escape(query))
    with open('students.txt', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            result = pattern.search(line)
            if result is None:
                file.write(line)
            file.truncate()


def all_students():
    with open('students.txt') as file:
        for line in file:
            print(line)


def find_class(query):
    with open('students.txt') as file:
        for line in file:
            if query in line:
                print(line)


def find_age(age):
    with open('students.txt') as file:
        for line in file:
            if age in line:
                print(line)


def average(mark):
    with open('students.txt') as file:
        for line in file:
            if int(mark) == round(float(line[-4:-1])):
                print(line)
