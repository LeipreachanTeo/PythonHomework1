# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
def sum_odd_pos_index(list):
    sum = 0
    for index, digit in enumerate(list):
        if index % 2 != 0:
            sum += digit
    return sum


list_digit = list(map(int, input("Введите список чисел через проблем: ").split()))
print(sum_odd_pos_index(list_digit))

