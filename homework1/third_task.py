# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
def plane_number(x, y):
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            return print('The point is in the first quarter of the plane')
        elif x < 0 and y > 0:
            return print('The point is in the second quarter of the plane')
        elif x < 0 and y < 0:
            return print('The point is in the third quarter of the plane')
        elif x > 0 and y < 0:
            return print('The point is in the fourth quadrant of the plane')
    else:
        return print('Enter where x or y is not equal to 0')


x,y = map(int, input("Ender points x and y. x and y != 0: ").split())

plane_number(x, y)