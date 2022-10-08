# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
def show_range_coordinate(quarter):
    if 1 <= quarter <= 4:
        if quarter == 1:
            return print(f'Range in first quarter for point x and point y: x > 0, y > 0')
        elif quarter == 2:
            return print(f'Range in second quarter for point x and point y: x < 0, y > 0')
        elif quarter == 3:
            return print(f'Range in third quarter for point x and point y: x < 0, y < 0')
        else:
            return print(f'Range in fourth quarter for point x and point y: x > 0, y < 0')
    else:
        return print(f'There is no such quarter plane')


quarter = int(input('Enter the number of the previous quarter from 1 to 4: '))
show_range_coordinate(quarter)