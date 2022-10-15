# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д
import math


def product_digit_opposite_index(list):
    last_index = -1
    start_index = 0
    product_list = []
    if len(list) % 2 == 0:
        while start_index < len(list) / 2:
            product_list.append(list[start_index]*list[last_index])
            start_index += 1
            last_index -= 1
    else:
        if start_index != math.ceil(len(list) / 2):
            while start_index < len(list) / 2:
                product_list.append(list[start_index]*list[last_index])
                start_index += 1
                last_index -= 1
        else:
            product_list.append(list[math.ceil(len(list) / 2)]**2)
    return product_list


list_digit = list(map(int, input("Введите список чисел через проблем: ").split()))
print(product_digit_opposite_index(list_digit))
