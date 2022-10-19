# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_non_repeating_element(lst):
    lst = list(map(int, lst))
    return [i for i in lst if lst.count(i) == 1]


N = input("Задайте последовательность цифр: ")

while not is_int(N):
    print('Введены не только цифры.')
    N = input("Задайте последовательность цифр: ")

print(is_non_repeating_element(N))
