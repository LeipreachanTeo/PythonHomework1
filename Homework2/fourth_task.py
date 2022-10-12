# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры
import random


def product_elements(first_index, second_index, N):
    lst = []

    def list_elements(digit):
        for i in range(-digit, digit + 1):
            lst.append(i)
        random.shuffle(lst)

    list_elements(N)
    print(f'список {lst} произведение элементов  first_index и second_index = {lst[first_index] * lst[second_index]}')


first_pos = int(input('Введите первую позицию: '))
second_pos = int(input('Введите первую позицию:'))
digit = int(input('Введите элемент:'))

product_elements(first_pos, second_pos, digit)
