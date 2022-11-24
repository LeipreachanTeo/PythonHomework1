from students_contacts import find_students, find_age, find_class, add_students, all_students, del_students, average

from choice import do_choice


def start():
    while True:
        selector = do_choice()
        if selector == 1:
            query = ((input('Для поиска ученика введите его фамилию: ').capitalize(),
                      input('Для поиска ученика введите его имя: ').capitalize()))
            print(find_students(query))
        elif selector == 2:
            add_students()
        elif selector == 3:
            query = ((input('Для удаления контакта введите его фамилию: ').capitalize(),
                      input('Для удаления контакта введите его имя: ').capitalize()))
            del_students(query)
        elif selector == 4:
            all_students()
        elif selector == 5:
            query = ((input('Для поиска учеников введите их номер класса: ').lower()))
            print(find_class(query))
        elif selector == 6:
            query = ((input('Для поиска учеников определенного возраста введите их год рождения: ')))
            print(find_age(query))
        elif selector == 7:
            query = ((input('Введите средний бал:  ')))
            print(average(query))
