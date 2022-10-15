# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(digit):
    f1, f2 = 1, 1
    list = [0]
    for i in range(digit):
        list.append(f1)
        f1, f2 = f2, f1+ f2
    f1, f2 = 1, -1
    for i in range(digit):
        list.insert(0, (f1))
        f1, f2 = f2, f1 - f2
    return list


digit = int(input("Введите целое число: "))

print(fibonacci(digit))



