# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def coding_file(file):
    f = open(file, 'r')
    text = f.read()
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res += str(f'<{count}>') + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res += str(f'<{count}>') + text[-1]
    f.close()
    f = open('Coding', 'w')
    f.write(res)
    f.close()
    return res

def decoding_file(file):
    f = open(file, 'r')
    text = f.read()
    number = ''
    res = ''
    for i in range(len(text)):
        if (not text[i].isalpha()) and text[i] !='>' and text[i] != '<':
            number += text[i]
        elif text[i] !='>' and text[i] != '<':
            res += text[i] * int(number)
            number = ''
    f.close()
    f = open('Decoding', 'w')
    f.write(res)
    f.close()
    return res



print(f"Текст после кодировки: {coding_file('text1.txt')}")
print(f"Текст после дешифровки: {decoding_file('text2.txt')}")
