# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

def esidual_difference(list):
    list_remainder= []
    for i in list:
        if i - int(i) != 0:
            list_remainder.append(i - int(i))
    return max(list_remainder) - min(list_remainder)


list_float = list(map(float, input("Введите список вещественных чисел через проблем: ").split()))
print(esidual_difference(list_float))


