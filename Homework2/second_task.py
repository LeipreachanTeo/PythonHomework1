# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def find_factorial(digit):
    digit = int(digit)
    start = 1
    lst_factorial = []
    if digit > 0:
        for i in range(1, digit + 1):
            start *= i
            lst_factorial.append(start)
        return lst_factorial
    elif digit == 0:
        return [1]


N = input("Введите положительное целое число: ")

while not is_int(N) :
    print('Введено не число.')
    N = input("Введите положительное целое число: ")

print(*find_factorial(N))
