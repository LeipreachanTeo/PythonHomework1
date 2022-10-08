# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
def find_distance(A,B):
    distance = ((B[0]- A[0])**2 + (B[1]-A[1])**2)**(0.5)
    print(f'distance between points A and B = {round(distance,3)}')


A = list(map(int,input("Enter the coordinates of point A(x and y) ").split()))
B = list(map(int,input("Enter the coordinates of point B(x and y)").split()))

find_distance(A,B)