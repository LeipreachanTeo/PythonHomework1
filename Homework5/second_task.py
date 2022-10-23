# Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
#
# b) Подумайте как наделить бота ""интеллектом""
from random import randint


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


number_candies = (input("Введите для игры количество конфет: "))

while not is_int(number_candies):
    print('Введено не целое число!!!')
    number_candies = input("Введите для игры количество конфет: ")
number_candies = int(number_candies)


def take_candy():
    count = int(input(f'Введите количество конфет которые собиретесь взять, их количество может быть от 1 до 28: '))
    while count < 1 or count > 28:
        count = int(input(f"Введите корректное количество конфет: "))
    return count


first_up = randint(0, 2)
if first_up:
    print('Ваш первый ход!')
else:
    print('Первый ход делает бот!')

while number_candies > 0:
    if first_up:
        print("Ваш ход")
        take = take_candy()
        number_candies -= take
        first_up = False
        print(f'На столе осталось {number_candies}  конфет')
    else:
        print("Ходит бот")
        bot_take = 0
        bot_take += number_candies - (number_candies//29)*29
        number_candies -= bot_take
        if bot_take:
            print(f'Бот взял {bot_take} конфет.На столе осталось {number_candies} конфет')
        else:
            bot_take = randint(1, 29)
            number_candies -= bot_take
            print(f'Бот взял {bot_take} конфет.На столе осталось {number_candies} конфет')
        first_up = True

if not first_up:
    print(f'ВЫ ПОБЕДИЛИ!!!')
else:
    print(f'ПОБЕДИЛ БОТ!!!')
