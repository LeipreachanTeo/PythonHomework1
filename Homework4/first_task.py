# Вычислить число Пи c заданной точностью d
def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def checking_number(digit):
    number = 1
    numbers_lst = []
    for i in range(10):
        number *= 0.1
        numbers_lst.append(round(number, i + 1))
    if float(digit) in numbers_lst:
        return True
    else:
        return False


def calculate_PI(digit):
    string = str(digit).split('.')
    k = 3
    pi = 0
    for i in range(1, 100000000, 4):
        pi += (4 / i) - (4 / k)
        k += 4
    return round(pi, len(string[1]))


digit = input("Введите число в диапозоне от 0.1 до 0.0000000001 с шагом *0.1: ")

while not is_float(digit) or not checking_number(digit):
    if not is_float(digit):
        print("Введено не вещественное число: ")
        digit = input("Введите вещественное число: ")
    else:
        print("Введено число не в диапозоне от 0.1 до 0.0000000001 с шагом *0.1:")
        digit = input("Введите вещественное число: ")

print(f"d={digit},π = {calculate_PI(digit)}")
