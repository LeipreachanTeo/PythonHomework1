# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            left_part = not(x or y or z)
            right_part = not x and not y and not z
            print(f' x ={x} y = {y} z = {z} ответ = {left_part == right_part}')