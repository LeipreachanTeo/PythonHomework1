# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
def search_weekend(week_number):
    if 0 < week_number <=5:
        return "workind day"
    elif  6 <= week_number <=7:
        return "weekend"
    else:
        return "number doesn't match the day of the week"


day = int(input("ender day of the week: "))

print(search_weekend(day))
