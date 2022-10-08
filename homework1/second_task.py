# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def check_predict(x, y, z):
    left_part = not (x or y or z)
    right_part = not x and not y and not z
    result = left_part == right_part
    return result


x, y, z = map(int, input('Ender x,y,z: ').split())

check_predict(x, y, z)

if check_predict(x, y, z) == True:
    print(f"Statement is True")
else:
    print(f"Statement if False")