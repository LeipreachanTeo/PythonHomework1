# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_word(file,word):
    f = open(file, 'r')
    text = f.read().split()
    def find_word():
        for i in text:
            if "абв" in i:
                text.remove(i)
                find_word()
    find_word()
    f.close()
    f = open(file, 'w')
    f.write(' '.join(text))
    f.close()
    return text

del_word('first_task.txt', 'абв')




