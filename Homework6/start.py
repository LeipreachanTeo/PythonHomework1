from contacts import find_contacts, add_contacts, del_contacts, all_contacts

from choice import do_choice


def start():
    while True:
        selector = do_choice()
        if selector == 1:
            query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
                      input('Для поиска контакта введите его имя: ').capitalize()))
            print(find_contacts(query))
        elif selector == 2:
            add_contacts()
        elif selector == 3:
            query = ((input('Для удаления контакта введите его фамилию: ').capitalize(),
                      input('Для удаления контакта введите его имя: ').capitalize()))
            del_contacts(query)
        elif selector == 4:
            all_contacts()
