# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
import random


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_funk(digit):
    string = ''
    for i in range(int(digit), -1, -1):
        N = random.randint(-100, 100)
        if i > 1:
            string += f"{N}x^{i}+"
            # s +=str(N)+'x'+'^'+str(i)+'+'
        elif i == 1:
            string += f'{N}x+'
        else:
            string += f'{N}=0'
    string = string.replace('+-', '-')
    return string


K = input('Введите положительное число: ')

while not is_int(K):
    print('Введено не число.')
    K = input("Введите положительное число: ")


funk = is_funk(K)
print(funk)
f = open('fourth_task.txt', 'w')
f.write(funk)
f.close()

