# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def sum_digit(n):
    return sum([int(i) for i in n if i.isdigit()])


digit = input("Введите вещественное число: ")

while not is_float(digit):
    if ',' in digit:
        print("Введено не вещественное число,вместо \",\" поставьте \".\" и повторите попытку")
        digit = input("Введите вещественное число: ")
    else:
        print("Введено не вещественное число, повторите ввод")
        digit = input("Введите вещественное число: ")

print(sum_digit(digit))
