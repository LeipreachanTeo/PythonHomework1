# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def calculate_prime_set(digit):
    lst = []
    digit = int(digit)
    for i in range(2, digit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            if digit % i == 0:
                lst.append(i)
    return lst


N = input('Введите натуральное число: ')

while not is_int(N):
    print('Введено не число.')
    N = input("Введите натуральное число: ")

print(calculate_prime_set(N))