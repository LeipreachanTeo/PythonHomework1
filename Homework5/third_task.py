# Создайте программу для игры в ""Крестики-нолики"".
from tkinter import *
import random, time


def stop_game():
    global game_left
    for item in game_left:
        buttons[item].config(bg='white', state='disabled')


def win(n):
    global game
    if (game[0] == n and game[1] == n and game[2] == n) or (game[3] == n and game[4] == n and game[5] == n) or (
            game[6] == n and game[7] == n and game[8] == n) \
            or (game[0] == n and game[3] == n and game[6] == n) or (game[1] == n and game[4] == n and game[7] == n) or (
            game[2] == n and game[5] == n and game[8] == n) \
            or (game[0] == n and game[4] == n and game[8] == n) or (game[2] == n and game[4] == n and game[6] == n):
        return True


def push(move):
    global game
    global game_left
    global turn
    game[move] = "X"
    buttons[move].config(text="X", bg='white', state='disabled')
    game_left.remove(move)
    if move == 4 and turn == 0:
        move_bot = random.choice(game_left)
    elif move != 4 and turn == 0:
        move_bot = 4
    if turn > 0:
        move_bot = 8 - move
    if move_bot not in game_left:
        try:
            move_bot = random.choice(game_left)
        except IndexError:
            label['text'] = 'Игра окончена'
            stop_game()
    game[move_bot] = '0'
    time.sleep(0.5)
    buttons[move_bot].config(text='0', bg='white', state='disabled')
    print(game)
    if win("X"):
        label['text'] = 'Вы победили!!!'
        stop_game()
    elif win('0'):
        label['text'] = 'Вы проиграли!!'
        stop_game()
    else:
        if len(game_left) > 1:
            game_left.remove(move_bot)
        else:
            label['text'] = 'Игра окончена'
            stop_game()
        turn += 1


game = [None] * 9
game_left = list(range(9))
turn = 0
root = Tk()
label = Label(width=20, text='Игра Крестики-нолики', font=('Arial', 20, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 28, 'bold'), bg='blue', command=lambda x=i: push(x)) for i in
           range(9)]

label.grid(row=0, column=0, columnspan=3)
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row += 1
        col = 0

root.mainloop()
