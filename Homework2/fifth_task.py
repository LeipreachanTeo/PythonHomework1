# 5) Реализуйте алгоритм перемешивания списка.
import random

def new_shuffle(lst):
    new_lst = []
    for i in lst:
        new_lst.insert(random.randrange(0,len(lst)),i)
    print(new_lst)

new_shuffle([1,2,3,4,5])


