# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def binary_digit(digit):
    return bin(digit)


def binary_digit2(digit):
    result = ''
    while digit > 0:
        result = str(digit % 2) + result
        digit //= 2
    return result


digit = int(input("Введите целое число: "))
print(binary_digit(digit))
print(binary_digit2(digit))