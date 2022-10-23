# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_word(file,word):
    f = open(file, 'r')
    text = f.read().split()
    def del_slovo():
        for i in text:
            if "абв" in i:
                text.remove(i)
                del_slovo()
    del_slovo()
    f.close()
    f = open(file, 'w')
    f.write(' '.join(text))
    f.close()
    return text

del_word('first_task.txt', 'абв')




