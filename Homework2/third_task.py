# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def sum_subsequence(digit):
    digit = int(digit)
    sum = 0
    for i in range(1, digit + 1):
        sum += (1 + 1 / i) ** i
    return sum


n = input("Введите целое число: ")

while not is_int(n):
    print('Введено не число.')
    n = input("Введите целое число: ")

print(round(sum_subsequence(n), 2))
