# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open('fifth_task1.txt')
f2 = open('fifth_task2.txt')
first_list = f1.read().replace(' ', '').replace('-', '+-').replace('=0', '')
second_list = f2.read().replace(' ', '').replace('-', '+-').replace('=0', '')

first_list = first_list.split('+')
second_list = second_list.split('+')
first_list_help = []
for i in first_list:
    first_list_help.append(i.split('x'))

second_list_help = []
for i in second_list:
    second_list_help.append(i.split('x'))

new_c = []
copy_first_list_help = first_list_help.copy()
copy_second_list_help = second_list_help.copy()
for i in first_list_help:
    for j in second_list_help:
        if len(i) > 1 and len(j) > 1:
            if i[1] == j[1]:
                new_c.append([int(i[0])+int(j[0]),i[1]])
                copy_first_list_help.remove(i)
                copy_second_list_help.remove(j)
        elif len(i) == 1 and len(j)==1:
            new_c.append([int(i[0])+int(j[0]),'^0'])
            copy_first_list_help.remove(i)
            copy_second_list_help.remove(j)


result = (new_c + copy_first_list_help + copy_second_list_help)
result_help = []
for i in result:
    i[0] = str(i[0])
result.sort(key=lambda x: x[1], reverse=True)
for i in result:
    first_list = ','.join(i)
    result_help.append(first_list.replace(',', 'x'))

finish = ','.join(result_help).replace(',', '+').replace('+-', '-').replace('x^0','')
finish += '=0'
f1.close()
f2.close()
f3 = open('result.txt','w')
f3.write(finish)
f3.close()
print(finish)


